import time
import tkinter
import tkinter.font
from pynotifier import Notification
from random import choice
from threading import Timer
import datetime


def it_is_time_for_notify():
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
    notifies = f"Time: {h}:{m}:{s} {meridian} -+- Date: {d}\n"
    return notifies


def notify(hours):
    """

    This Function notifies when it's an hour, two hours or more.

    """
    present = it_is_time_for_notify()
    if hours == 1:
        Notification("It's an Hour!!", present).send()
    else:
        ptr = f"It's {hours} Hours"
        Notification(ptr, present).send()
    Timer(3600, function=lambda: notify(hours + 1)).start()


def snooze(window):
    """

    This Function snoozes for 5min and then again shows the 'Break' Window.

    """
    window.destroy()
    time.sleep(300)
    App()


def go_next(window):
    """

    This Function Destroys the 'Break' Window.

    """
    window.destroy()


class App(tkinter.Tk):
    """

    This Class is inherited from tkinter.Tk, creates and configures the window whilst updating the clock on display.

    """

    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        self.title("20-20-20")
        self.lab = tkinter.Label(
            self,
            text="Every 20 minutes, look at something 20 feet away for 20 seconds.".center(
                80
            ),
            font=tkinter.font.Font(size=15),
        )
        self.geometry("700x220")
        file = open("quotes.txt", "r")
        lst = file.read().splitlines()
        quote = choice(lst)
        self.quote_lab = tkinter.Label(
            self, text=quote.center(80), font=tkinter.font.Font(size=10)
        )
        self.present_lab = tkinter.Label(
            self, text=it_is_time_for_notify(), font=tkinter.font.Font(size=15)
        )
        self.lab.grid(column=0, row=0)
        self.quote_lab.grid(column=0, row=4)
        self.present_lab.grid(column=0, row=1)
        selfWidth = self.winfo_reqwidth()
        selfHeight = self.winfo_reqheight()
        positionRight = int(self.winfo_screenwidth() / 2 - selfWidth)
        positionDown = int(self.winfo_screenheight() / 2 - selfHeight)
        self.geometry("+{}+{}".format(positionRight, positionDown))
        self.attributes("-topmost", True)
        bt1 = tkinter.Button(
            self,
            text="Snooze for 5 min",
            padx=1,
            pady=5,
            command=lambda: snooze(self),
            font=tkinter.font.Font(size=15),
        )
        bt1.grid(column=0, row=2)
        bt2 = tkinter.Button(
            self,
            text="Go for Next Break",
            padx=1,
            pady=5,
            command=lambda: go_next(self),
            font=tkinter.font.Font(size=15),
        )
        bt2.grid(column=0, row=3)
        self.update_clock()
        self.mainloop()

    def update_clock(self):
        """

        This function updates the clock displayed on the window.

        """
        self.present_lab.configure(text=it_is_time_for_notify())
        self.after(1000, self.update_clock)


def main():
    """

    This function initializes the Hour Timer and Break Timer.

    """
    Notification("Started Timer...", " ").send()
    Timer(3600, function=lambda: notify(1)).start()
    while True:
        time.sleep(1200)
        App()


main()
