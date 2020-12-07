from win10toast import ToastNotifier
import subprocess
import time


def get_level():
    """

    Returns the Battery Level of the Laptop in Integer

    """
    bat = subprocess.run("WMIC PATH Win32_Battery Get EstimatedChargeRemaining", shell=True, capture_output=True)
    cat = bat.stdout.decode()
    level = int(cat.split("\n")[1].strip())
    return level


def get_status():
    """

    Returns the Charging Status of the Laptop in Integer
    1 - Discharging
    2 - Charging

    """
    dat = subprocess.run("WMIC PATH Win32_Battery Get BatteryStatus", shell=True, capture_output=True)
    eat = dat.stdout.decode()
    charge = int(eat.split("\n")[1].strip())
    return charge


def main():
    """
    This is the Main Function where the Level and Status is analysed and Notifications are displayed by checking
    them every 5 seconds. If a wrong input is received from command console it will be terminated if it is occurred
    5 times. You will be Notified if the Charging is less than 30%, more than 80% and also during the transition of
    Charging Status like you will be notified by the Charging time and % of Battery decreased or increased.

    """
    last_level = 0
    last_charge = 0
    lsc = get_level()  # It is the level recorded when the charging phase changes
    pt = ToastNotifier()
    wrong_outputs = 0
    start = time.time()
    while wrong_outputs < 5:
        level = get_level()
        charge = get_status()
        if charge == 1:
            if level < 30 and level != last_level:
                notify = f"BATTERY LEVEL: {level}"
                pt.show_toast("LOW BATTERY!! Charge it now...", notify, duration=5)
            elif last_charge == 2:
                end = time.time() - start
                notify = f"It took {round(end / 60, 1)}min to charge {level - lsc}%"
                pt.show_toast("Charging Stopped...", notify, f"BATTERY LEVEL: {level}")
                lsc = level
                start = time.time()
        elif charge == 2:
            if level > 80 and level != last_level:
                notify = f"Stop Charging the battery now..."
                pt.show_toast(notify, f"BATTERY LEVEL: {level}")
            elif last_charge == 1:
                end = time.time() - start
                tt = f"{abs(lsc - level)}% Charge for {round(end / 60, 1)}min"
                lsc = level
                start = time.time()
                notify = f"Started Charging..."
                pt.show_toast(tt, notify, f"BATTERY LEVEL: {level}")
        else:
            notify = "Something wrong output is received!!!"
            pt.show_toast(notify)
            wrong_outputs += 1
        last_level = level
        last_charge = charge
        time.sleep(5)  # Iterates Every 5 seconds


main()
