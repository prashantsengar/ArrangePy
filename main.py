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

class CHOICES:
    WEAK = 1
    STRONG = 2
    EXIT = 0

def main(root, choice=None, warn_for_strong=False):
    
    destination = os.path.join(TARGET_FOLDER, RESULT_DIR)
    lib.utils.makeFolders(destination, FOLDER_TYPES.keys())

    print("---ArrangePy---")
    print("Cleaning: ", root)

    if choice is None:
        choice = int(
            input(
                "Press [1]: for Weak arrange"
                + "\nPress [2]: for Strong arrange"
                + "\nPress [0]: to exit\nOption: "
            )
        )

    if choice == CHOICES.WEAK:
        res = lib.arrange.weak_arrange(root, destination, FOLDER_TYPES)
    elif choice == CHOICES.STRONG:
        res = lib.arrange.strong_arrange(root, destination, FOLDER_TYPES, warn_for_strong)
    elif choice == CHOICES.EXIT:
        return
    else:
        print("Incorrect Input")
        return

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

if __name__ == "__main__":
    main(TARGET_FOLDER)
