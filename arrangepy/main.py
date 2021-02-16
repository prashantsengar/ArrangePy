# ArrangePy
# Arranges the files according to their types for later classification
# https://github.com/prashantsengar/ArrangePy
# https://t.me/joinchat/INDdLlDf-SFDPURESGgdrQ

import os
import sys
from . import func
from . import utils
from . import web as webapp

import argparse


RESULT_DIR = "ArrangedPy"
FOLDER_TYPES = utils.configure()

class CHOICES:
    WEAK = 1
    STRONG = 2
    EXIT = 0

def run(root, choice=None, warn_for_strong=True):
    TARGET_FOLDER = root
    destination = os.path.join(TARGET_FOLDER, RESULT_DIR)
    # print(destination)
    utils.makeFolders(destination, FOLDER_TYPES.keys())

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
        res = func.weak_arrange(root, destination, FOLDER_TYPES)
    elif choice == CHOICES.STRONG:
        res = func.strong_arrange(root, destination, FOLDER_TYPES, warn_for_strong)
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

def main():
    parser = argparse.ArgumentParser()

    exclusive_group = parser.add_mutually_exclusive_group()

    exclusive_group.add_argument(
        "-w", "--weak", action="store_true", required=False, help="Weak arrange"
    )
    exclusive_group.add_argument(
        "-s", "--strong", action="store_true", required=False, help="Strong arrange"
    )
    exclusive_group.add_argument(
        "-b", "--web", action="store_true", required=False, help="Run web GUI"
    )

    parser.add_argument(
        "directory",
        nargs="?",
        help="The directory to arrange, default is current working directory",
    )
    parser.add_argument(
        "-nw",
        "--no-warning",
        action="store_true",
        required=False,
        help="Don't show any warnings when running strong arrange",
    )

    args = parser.parse_args()
    target = os.getcwd()

    if args.directory:
        target = args.directory
    if args.web:
        webapp.main(target=target)
    elif args.weak:
        run(target, choice=CHOICES.WEAK)
    elif args.strong:
        run(target, choice=CHOICES.STRONG, warn_for_strong=args.no_warning)
    else:
        run(target)


if __name__ == "__main__":
    main()
