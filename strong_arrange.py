import os
from move_files import *
from configure import configur

RESULT_DIR = "CleanedPy"
FOLDER_TYPES = configur()


def strong_arrange(root, destination, index):
    TOTAL_COUNT = {}
    for foldername, subfolders, filenames in os.walk(root):
        for file in filenames:
            if os.path.isfile(os.path.join(foldername, file)):
                status, types = startProcess(foldername, file, index, destination)
                if types in TOTAL_COUNT:
                    TOTAL_COUNT[types] = TOTAL_COUNT[types] + 1
                else:
                    TOTAL_COUNT[types] = 1
    return TOTAL_COUNT


# print(strong_arrange(sys.argv[1],RESULT_DIR,FOLDER_TYPES))
