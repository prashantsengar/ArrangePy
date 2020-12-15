import os
from move_files import *
from configure import configur

RESULT_DIR = "CleanedPy"
FOLDER_TYPES = configur()


def weak_arrange(root, destination, index):
    TOTAL_COUNT = {}
    for file in os.listdir(root):
        if os.path.isfile(os.path.join(root, file)):
            status, types = startProcess(root, file, index, destination)
            if types in TOTAL_COUNT:
                TOTAL_COUNT[types] = TOTAL_COUNT[types] + 1
            else:
                TOTAL_COUNT[types] = 1
    return TOTAL_COUNT


# print(weak_arrange(sys.argv[1],RESULT_DIR,FOLDER_TYPES))
