import os
from move_files import *
from configure import configur
import sys
import time

RESULT_DIR = "CleanedPy"
FOLDER_TYPES = configur()


def strong_arrange(root, destination, index,warn=True):
    if warn == True:
        print("You are going to strong arrange",
              "the directory DIRECTORY_NAME.",
              "It will rearrange all the files",
              "in the subfolders as well.",
              "It might cause issues if you",
              "have added wrong extensions",
              "in the config.ini file and run",
              "the program in a sensitive directory.",
              "You still have 10 seconds to",
              "cancel it if you want to review anything.",
              "\n(Press Ctrl+C to abort)")
        try:
            time.sleep(10)
        except KeyboardInterrupt:
            sys.exit()
            return False
    
    TOTAL_COUNT = {}
    for foldername, subfolder, filenames in os.walk(root):
        for file in filenames:
            if os.path.isfile(os.path.join(foldername, file)):
                status, types = startProcess(foldername, file, index, destination)
                if types in TOTAL_COUNT:
                    TOTAL_COUNT[types] = TOTAL_COUNT[types] + 1
                else:
                    TOTAL_COUNT[types] = 1
    return TOTAL_COUNT


# print(strong_arrange(sys.argv[1],RESULT_DIR,FOLDER_TYPES))
