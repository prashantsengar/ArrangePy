import time
import datetime
from win10toast_persist import ToastNotifier


def it_is_time():
    """

    This Function returns the Current Time and Date with the Standard Format in a String.

    """
    now = datetime.datetime.now()
    h = now.hour
    m = now.minute
    s = now.second
    d = "-".join(str(now.date()).split("-")[::-1])
    meridian = "AM"
    if h > 12:
        h = h - 12
        meridian = "PM"
    notifies = f"Time: {h}:{m}:{s} {meridian}\nDate: {d}\n"
    return notifies


def main():
    """

    This Function Notifies every half-an-hour.
    If it's 0.5, 1.5, 2.5, etc hr it notifies the Current Date and Time.
    If it's 1, 2, 3.. hr it notifies how many hrs that's been passed. Every count starts from the beginning of
    execution of the program.

    """
    toaster = ToastNotifier()
    n = 0
    notify = "Timer Started"
    toaster.show_toast(notify, duration=5)
    while n < 12:
        time.sleep(1800)
        toaster.show_toast(it_is_time(), duration=5)
        time.sleep(1800)
        n += 1
        if n == 1:
            nof = "It's one hour"
        else:
            nof = f"It's {n} hours"
        toaster.show_toast(nof, it_is_time(), duration=5)


main()
