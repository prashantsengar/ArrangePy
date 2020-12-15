# arrange.py
# Arranges the fiels according to their types for later classification

import os
import sys
from move_files import *
from configure import configur
from strong_arrange import strong_arrange
from weak_arrange import weak_arrange
from make_folders import makeFolders

RESULT_DIR = "CleanedPy"
FOLDER_TYPES = configur()

try:
    TARGET_FOLDER = sys.argv[1]
except:
    TARGET_FOLDER = os.getcwd()

if __name__ == "__main__":

    root = TARGET_FOLDER
    destination = os.path.join(TARGET_FOLDER, RESULT_DIR)
    makeFolders(destination, FOLDER_TYPES.keys())

    print("Arrange files")
    print("Cleaning:", root)

    choice = int(
        input(
            "Press [1]: for Weak arrange\nPress [2]: for Strong arrange\n[0]: to exit\nOption: "
        )
    )

    if choice == 1:
        res = weak_arrange(root, destination, FOLDER_TYPES)
    elif choice == 2:
        res = strong_arrange(root, destination, FOLDER_TYPES)
    elif choice == 0:
        sys.exit()
    else:
        print("Incorrect Input")
        sys.exit()

    # Final Result
    message = "Result"
    others = "Others(Not_moved)"
    print(f"{message:*^30s}")
    for key, value in res.items():
        if key == others:
            continue
        print(f"{value} file moved into Category {key}")
    if others in res:
        print(f"{res[others]} file Not moved")
