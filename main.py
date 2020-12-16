# arrange.py
# Arranges the fiels according to their types for later classification

import os
import sys
import bin.arrange
import bin.utils


RESULT_DIR = "CleanedPy"
FOLDER_TYPES = bin.utils.configur()

try:
    TARGET_FOLDER = sys.argv[1]
except:
    TARGET_FOLDER = os.getcwd()

if __name__ == "__main__":

    root = TARGET_FOLDER
    destination = os.path.join(TARGET_FOLDER, RESULT_DIR)
    bin.utils.makeFolders(destination, FOLDER_TYPES.keys())

    print("Arrange files")
    print("Cleaning:", root)

    choice = int(
        input(
            "Press [1]: for Weak arrange\nPress [2]: for Strong arrange\nPress [0]: to exit\nOption: "
        )
    )

    if choice == 1:
        res = bin.arrange.weak_arrange(root, destination, FOLDER_TYPES)
    elif choice == 2:
        res = bin.arrange.strong_arrange(root, destination, FOLDER_TYPES)
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
