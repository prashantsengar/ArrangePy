import time
import psutil
from pynotifier import Notification
import pandas as pd
import datetime
import numpy as np
import os


def get_info():
    """
    This Function uses the psutil module to get the status of Battery.
    :return:
    Percentage of Battery, State of Battery, Secs_left for remaining battery
    """
    battery = psutil.sensors_battery()
    percent = int(battery.percent)
    secs_left = int(battery.secsleft)
    state = str(battery.power_plugged)
    return percent, state, secs_left


def main(file):
    """
    This is the Main Function where the Level and Status is analysed and Notifications are displayed by checking
    them every 5 seconds. If a wrong input is received from command console it will be terminated if it is occurred
    5 times. You will be Notified if the Charging is less than 30%, more than 80% and also during the transition of
    Charging Status like you will be notified by the Charging time and % of Battery decreased or increased. Also usage
    stats are saved for further need.

    """
    last_level = 0
    last_charge = 0
    cpu_usage = []
    cpu_freq = []
    ram_usage = []
    lsc, _, __ = get_info()  # It is the level recorded when the charging phase changes
    wrong_outputs = 0
    Notification("Started Battery Program...", " ", duration=2).send()
    start = time.time()
    while wrong_outputs < 5:
        level, charge, _ = get_info()
        if charge == "False":
            if level < 30 and level != last_level:
                notify = f"BATTERY LEVEL: {level}"
                Notification(
                    "LOW BATTERY!! Charge it now...", notify, duration=5
                ).send()
            elif last_charge == "True":
                end = time.time() - start
                notify = f"It took {round(end / 60, 1)}min to charge {level - lsc}%"
                Notification(
                    "Charging Stopped...", notify + f"  BATTERY LEVEL: {level}"
                ).send()
                start = time.time()
                data = {
                    "Date": [datetime.datetime.now().strftime("%x")],
                    "Time": [datetime.datetime.now().strftime("%X")],
                    "Level": [level],
                    "Status": ["charging"],
                    "Charge %": [abs(level - lsc)],
                    "Minutes": [round(end / 60, 1)],
                    "From": [lsc],
                    "To": [level],
                    "CPU_Usage": [round(int(np.mean(cpu_usage)), 2)],
                    "CPU_Frequency": [round(int(np.mean(cpu_freq)), 2)],
                    "Cores": [psutil.cpu_count(logical=True)],
                    "RAM_Usage": [round(int(np.mean(ram_usage)), 2)],
                }
                write_to_file(data, file)
                cpu_usage = []
                cpu_freq = []
                ram_usage = []
                lsc = level
        elif charge == "True":
            if level > 80 and level != last_level:
                notify = f"Stop Charging the battery now..."
                Notification(notify, f"BATTERY LEVEL: {level}").send()
            elif last_charge == "False":
                end = time.time() - start
                tt = f"{abs(lsc - level)}% Charge for {round(end / 60, 1)}min"
                start = time.time()
                data = {
                    "Date": [datetime.datetime.now().strftime("%x")],
                    "Time": [datetime.datetime.now().strftime("%X")],
                    "Level": [level],
                    "Status": ["discharging"],
                    "Charge %": [abs(level - lsc)],
                    "Minutes": [round(end / 60, 1)],
                    "From": [lsc],
                    "To": [level],
                    "CPU_Usage": [round(int(np.mean(cpu_usage)), 2)],
                    "CPU_Frequency": [round(int(np.mean(cpu_freq)), 2)],
                    "Cores": [psutil.cpu_count(logical=True)],
                    "RAM_Usage": [round(int(np.mean(ram_usage)), 2)],
                }
                write_to_file(data, file)
                lsc = level
                notify = f"Started Charging..."
                Notification(tt, notify + f"  BATTERY LEVEL: {level}").send()
        else:
            notify = "Something wrong output is received!!!"
            Notification(notify, " ").send()
            wrong_outputs += 1
        last_level = level
        last_charge = charge
        cpu_freq.append(psutil.cpu_freq().current)
        ram_usage.append(psutil.virtual_memory().percent)
        cpu_usage.append(psutil.cpu_percent(interval=4))


def write_to_file(new_data, file):
    """

    This function writes the data to a csv file with the given name.
    :param new_data: The Data that's need to be appended to the existing file.
    :param file: The file which the data will be written.

    """
    rf = pd.read_csv(file)
    cols = rf.columns
    rf = dict(rf)
    for x in cols:
        rf[x] = list(rf[x]) + list(new_data[x])
    pf = pd.DataFrame(rf)
    pf.to_csv(file, index=False)


def start_fn():
    """

    Creates a file and start the main fn.

    """
    file = "log.csv"
    if not os.path.isfile(file):
        new_data = {
            "Date": [],
            "Time": [],
            "Level": [],
            "Status": [],
            "Charge %": [],
            "Minutes": [],
            "From": [],
            "To": [],
            "CPU_Usage": [],
            "CPU_Frequency": [],
            "Cores": [],
            "RAM_Usage": [],
        }
        df = pd.DataFrame.from_dict(new_data)
        df.to_csv(file, index=False)
    main(file)


start_fn()
