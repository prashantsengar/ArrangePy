import os
from . import utils
import sys
import time


def strong_arrange(root, destination, index, warn=True):
    """
    Deploys strong arrange function that arranges files
    from current folder and subfolders into specified categories

    """
    if warn is True:
        print(
            "You are going to strong arrange",
            f"the directory {root}.",
            "It will rearrange all the files",
            "in the subfolders as well.",
            "It might cause issues if you",
            "have added wrong extensions",
            "in the config.ini file and run",
            "the program in a sensitive directory.",
            "You still have 7 seconds to",
            "cancel it if you want to review anything.",
            "\n(Press Ctrl+C to abort)",
        )
        try:
            time.sleep(7)
        except KeyboardInterrupt:
            sys.exit()

    TOTAL_COUNT = {}
    for foldername, subfolder, filenames in os.walk(root):
        for file in filenames:
            if os.path.isfile(os.path.join(foldername, file)):
                status, types = utils.startProcess(
                    foldername, file, index, destination
                )
                if types in TOTAL_COUNT:
                    TOTAL_COUNT[types] = TOTAL_COUNT[types] + 1
                else:
                    TOTAL_COUNT[types] = 1
    return TOTAL_COUNT


def weak_arrange(root, destination, index):
    """
    Deploys weak arrange function that arranges files only
    from current folder into specified categories

    """
    TOTAL_COUNT = {}
    for file in os.listdir(root):
        if os.path.isfile(os.path.join(root, file)):
            status, types = utils.startProcess(root, file, index, destination)
            if types in TOTAL_COUNT:
                TOTAL_COUNT[types] = TOTAL_COUNT[types] + 1
            else:
                TOTAL_COUNT[types] = 1
    return TOTAL_COUNT
