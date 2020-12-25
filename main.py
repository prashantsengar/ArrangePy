# CleanPy
# Arranges the files according to their types for later classification
# https://github.com/prashantsengar/CleanPy
# https://t.me/joinchat/INDdLlDf-SFDPURESGgdrQ

import os
import errno
import sys
import lib.arrange
import lib.utils
import argparse

RESULT_DIR = "CleanedPy"
FOLDER_TYPES = lib.utils.configure()

if __name__ == "__main__":
    # Using argparse for the CLI.
    # This is where we take inputs from the user. In the CLI , we shall expect the following
    # 1) Target directory is a required option
    # 2) Default option of arrange is strong , which we will warn the user before executing.
    # 3) He can over ride default with --arrange=weak. --arrange=strong also shall work.
    # 4) Warnings and user prompts can be escaped using --nowarn

    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("clean_dir", help="The directory which you want to clean up")
    # help for arrange
    arrange_help = """ Different modes of clean up 
    1) strong 
    2) weak 
    Defaults to strong """
    parser.add_argument("-a", "--arrange", type=str, help=arrange_help)
    parser.add_argument(
        "-nw", "--nowarning", action="store_true", help="flag to skip all the warnings"
    )
    args = parser.parse_args()
    TARGET_FOLDER = args.clean_dir
    if not os.path.isdir(TARGET_FOLDER):
        # print(" The provided directory for cleaning is not a valid path")
        raise OSError(errno.ENOENT, "No such file or directory", TARGET_FOLDER)
    destination = os.path.join(TARGET_FOLDER, RESULT_DIR)
    lib.utils.makeFolders(destination, FOLDER_TYPES.keys())

    print(f"---CleanPy Activated on {TARGET_FOLDER}---")

    if args.arrange:
        if args.arrange == "strong":
            choice = 2
        elif args.arrange == "weak":
            choice = 1
        else:
            raise OSError(errno.EINVAL, "Arrange value must either be strong or weak")
    else:
        print("Arrange value defaulting to strong ")
        choice = 2
    warn = True
    if args.nowarning:
        warn = False
    if choice == 1:
        res = lib.arrange.weak_arrange(TARGET_FOLDER, destination, FOLDER_TYPES)
    elif choice == 2:
        res = lib.arrange.strong_arrange(
            TARGET_FOLDER, destination, FOLDER_TYPES, warn=warn
        )

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
