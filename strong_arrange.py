import os
from move_files import *
from configure import configur

RESULT_DIR = "CleanedPy"
FOLDER_TYPES = configur()


def strong_arrange(root, destination, index):
    try:
        X = int(input("ARE YOU SURE YOU WANT TO PERFORM A STRONG ARRANGE?\n(Enter \"1\" to confirm, \"0\" to exit)"))
    except:
        X = 0
    if not X == 1:
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
