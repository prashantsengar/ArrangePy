import os
import pandas as pd
import time
import tkinter
import tkinter.font
import threading
from tkinter import filedialog


class file_data:
    def __init__(self):
        self.name = os.getcwd()
        self.size = 0.0
        self.ext = "B"

    def __lt__(self, other):
        return self.size > other.size


class data:
    def __init__(self, path):
        self.path = path
        self.file_lst = []
        self.x = 0
        self.info = []
        self.thread = threading.Thread(target=self.walk_dir())
        self.thread.start()
        self.complete = False
        self.now = " "

    def walk_dir(self):
        for folderName, sub_folders, filenames in os.walk(self.path):
            for filename in filenames:
                pt = file_data()
                pt.name = os.path.join(folderName, filename)
                ext = os.stat(pt.name)
                pt.size = ext.st_size
                self.file_lst.append(pt)
                self.x += 1
                self.now = pt.name
        self.sort_and_normalize()

    def sort_and_normalize(self):
        self.file_lst.sort()
        extensions = ["B", "KB", "MB", "GB", "TB"]
        p = 0
        self.info = [["Name", "Size", "Units"]]
        for element in self.file_lst:
            i = 0
            p += element.size
            while element.size > 1024.0:
                element.size = element.size / 1024
                i += 1
            element.size = round(element.size, 3)
            element.ext = extensions[i]
            self.info.append([element.name, element.size, element.ext])
        self.complete = True


class App(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        self.title("Large Files Info")
        self.path = " "
        self.now = tkinter.StringVar()
        self.now.set(" ")
        self.total = tkinter.IntVar()
        self.total.set(0)
        self.info = []
        self.file_lst = []
        self.table_data = []
        self.lst = []
        self.table_index = tkinter.IntVar()
        self.table_index.set(0)
        self.thread = ""
        self.x = tkinter.IntVar()
        self.x.set(0)
        self.complete = False
        self.geometry("980x500")
        selfWidth = self.winfo_reqwidth()
        selfHeight = self.winfo_reqheight()
        positionRight = int(self.winfo_screenwidth() / 2 - 2 * selfWidth)
        positionDown = int(self.winfo_screenheight() / 2 - selfHeight)
        self.geometry("+{}+{}".format(positionRight, positionDown))
        # self.attributes("-topmost", True)
        bt1 = tkinter.Button(
            self,
            text="Choose the folder to Scan (Browse)".center(50, "+"),
            padx=1,
            pady=5,
            command=self.browse_dir,
            font=tkinter.font.Font(size=15),
        )
        bt1.grid(column=0, row=0)
        self.folder = tkinter.Label(
            self, text="Folder Chosen: " + self.path, font=tkinter.font.Font(size=10)
        )
        self.folder.grid(column=1, row=0)
        self.file = tkinter.Label(
            self,
            text=str("Scanning: " + self.now.get()).center(50),
            font=tkinter.font.Font(size=10),
        )
        self.file.grid(column=0, row=1)
        self.count = tkinter.Label(
            self,
            text=str(
                "Scanned: "
                + str(self.x.get())
                + "  Total Size: "
                + str(self.total.get())
            ).center(50),
            font=tkinter.font.Font(size=10),
        )
        self.count.grid(column=1, row=1)
        self.t1 = tkinter.Label(self, text="   ", font=tkinter.font.Font(size=14))
        self.t1.grid(column=0, row=2)
        self.t2 = tkinter.Label(self, text="   ", font=tkinter.font.Font(size=12))
        self.t2.grid(column=0, row=3)
        self.t3 = tkinter.Label(self, text="   ", font=tkinter.font.Font(size=12))
        self.t3.grid(column=1, row=3)
        for x in range(4, 14):
            self.lst.append([])
            for y in range(2):
                top = tkinter.Label(self, text=" ", font=tkinter.font.Font(size=10))
                top.grid(column=y, row=x)
                self.lst[-1].append(top)
        self.mainloop()

    def browse_dir(self):
        self.t1.configure(text="  ")
        self.t2.configure(text="  ")
        self.t3.configure(text="  ")
        for x in range(10):
            self.lst[x][0].configure(text="  ")
            self.lst[x][1].configure(text="  ")
        self.path = " "
        self.now = tkinter.StringVar()
        self.now.set(" ")
        self.total = tkinter.IntVar()
        self.total.set(0)
        self.table_data = []
        self.table_index = tkinter.IntVar()
        self.table_index.set(0)
        self.info = []
        self.file_lst = []
        self.thread = ""
        self.x = tkinter.IntVar()
        self.x.set(0)
        self.complete = False
        self.path = filedialog.askdirectory()
        # self.update_clock()
        pqr = "Folder Chosen: " + self.path
        if len(pqr) >= 65:
            pqr = pqr[:30] + "..." + pqr[-30:]
        self.folder.configure(text=pqr)
        self.thread = threading.Thread(target=self.walk_dir)
        self.thread.start()

    def update_display(self):
        """

        This function updates the clock displayed on the window.

        """
        d = "Scanning: " + str(self.now.get())
        if len(d) <= 50:
            d = d.center(50)
        else:
            d = d[:23] + "..." + d[-24:]
            d.center(50)
        self.file.configure(text=d)
        pg = self.total.get()
        i = 0
        extensions = ["B", "KB", "MB", "GB", "TB"]
        while pg > 1024.0:
            pg /= 1024
            i += 1
        pg = round(pg, 3)
        pg = "  Total Size: " + str(pg) + " " + str(extensions[i])
        self.count.configure(text=str("Scanned: " + str(self.x.get()) + pg).center(50))
        # Timer(2, function=self.update_clock).start()

    def walk_dir(self):
        st = time.time()
        ptr = 0
        for folderName, sub_folders, filenames in os.walk(self.path):
            for filename in filenames:
                pt = file_data()
                pt.name = os.path.join(folderName, filename)
                ext = os.stat(pt.name)
                pt.size = ext.st_size
                self.file_lst.append(pt)
                self.now.set(pt.name)
                ptr += pt.size
                self.total.set(ptr)
                self.x.set(self.x.get() + 1)
                if time.time() - st > 1:
                    self.update_display()
                    st = time.time()
        self.update_display()
        self.sort_and_normalize()

    def sort_and_normalize(self):
        pst = self.file_lst
        pst.sort()
        extensions = ["B", "KB", "MB", "GB", "TB"]
        p = 0
        self.table_data.append([])
        self.info = [["Name", "Size", "Units"]]
        for element in pst:
            i = 0
            while element.size > 1024.0:
                element.size = element.size / 1024
                i += 1
            element.size = round(element.size, 3)
            element.ext = extensions[i]
            self.info.append([element.name, element.size, element.ext])
            self.table_data[-1].append([element.name, element.size, element.ext])
            p += 1
            if p == 10:
                p = 0
                self.table_data.append([])
        self.complete = True
        self.file.configure(text="Scanning Completed")
        self.display_table()

    def update_table(self, n):
        if self.complete:
            if n == 1:
                if self.table_index.get() < len(self.table_data) - 1:
                    self.table_index.set(self.table_index.get() + 1)
            else:
                if self.table_index.get() > 0:
                    self.table_index.set(self.table_index.get() - 1)
            for x in range(len(self.table_data[self.table_index.get()])):
                pg = self.table_data[self.table_index.get()][x][0]
                pg = pg[:23] + "..." + pg[-24:]
                self.lst[x][0].configure(text=pg.ljust(50))
                self.lst[x][1].configure(
                    text=str(self.table_data[self.table_index.get()][x][1]).ljust(2, " ")
                    + "        "
                    + self.table_data[self.table_index.get()][x][2].ljust(2, " ")
                )
            for x in range(len(self.table_data[self.table_index.get()]), 10):
                self.lst[x][0].configure(text="  ")
                self.lst[x][1].configure(text="  ")

    def display_table(self):
        self.t1.configure(text="Listing of Files")
        self.t2.configure(text="Name of the File")
        self.t3.configure(text="Size        Unit")
        for x in range(len(self.table_data[self.table_index.get()])):
            pg = self.table_data[self.table_index.get()][x][0]
            pg = pg[:23] + "..." + pg[-24:]
            self.lst[x][0].configure(text=pg.ljust(50))
            self.lst[x][1].configure(
                text=str(self.table_data[self.table_index.get()][x][1]).ljust(6, " ")
                + "        "
                + self.table_data[self.table_index.get()][x][2].ljust(2, " ")
            )
        bt_next = tkinter.Button(
            self,
            text="Next 10->".center(50, " "),
            padx=1,
            pady=5,
            command=lambda: self.update_table(1),
            font=tkinter.font.Font(size=12),
        )
        bt_next.grid(column=1, row=14)
        bt_prev = tkinter.Button(
            self,
            text="<-Previous 10".center(50, " "),
            padx=1,
            pady=5,
            command=lambda: self.update_table(-1),
            font=tkinter.font.Font(size=12),
        )
        bt_prev.grid(column=0, row=14)


App()
