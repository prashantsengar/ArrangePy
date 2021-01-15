# ArrangePy
# Arranges the files according to their types for later classification
# https://github.com/prashantsengar/ArrangePy
# https://t.me/joinchat/INDdLlDf-SFDPURESGgdrQ

import os
import sys
import lib.arrange
import lib.utils

RESULT_DIR = "CleanedPy"
FOLDER_TYPES = lib.utils.configure()

try:
    TARGET_FOLDER = sys.argv[1]
except:
    TARGET_FOLDER = os.getcwd()

if __name__ == "__main__":

    root = TARGET_FOLDER
    destination = os.path.join(TARGET_FOLDER, RESULT_DIR)
    lib.utils.makeFolders(destination, FOLDER_TYPES.keys())

    print("---ArrangePy---")
    print("Cleaning: ", root)

    choice = int(
        input(
            "Press [1]: for Weak arrange"
            + "\nPress [2]: for Strong arrange"
            + "\nPress [0]: to exit\nOption: "
        )
    )

    if choice == 1:
        res = lib.arrange.weak_arrange(root, destination, FOLDER_TYPES)
    elif choice == 2:
        res = lib.arrange.strong_arrange(root, destination, FOLDER_TYPES)
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
