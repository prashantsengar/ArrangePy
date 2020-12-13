# arrange.py
# Arranges the fiels according to their types for later classification

import os
import sys
import shutil
import configparser
import re
import sys
from move_files import *
from configure import configur
from strong_arrange import strong_arrange
from weak_arrange import weak_arrange
'''
Takes Command Line Argument for File Location.
Defaults to Current location if not specified
'''
RESULT_DIR = 'CleanedPy'
try:
    RESULT_DIR = os.path.join(sys.argv[1],RESULT_DIR)
except:
    pass

FOLDER_TYPES = configur()

if __name__ == '__main__':

    print("Arrange files")
    try:
        folder = sys.argv[1]
    except:
        folder = os.getcwd()
    print(folder)

    choice = int(input("Press 1 for Weak arrange\nPress 2 for Strong arrange\n0 to exit\noption:"))

    if choice == 1:
        res = weak_arrange(folder,RESULT_DIR,FOLDER_TYPES)
    if choice == 2:
        res = strong_arrange(folder,RESULT_DIR,FOLDER_TYPES)
    if choice == 0:
        sys.exit()

    # Final Result
    message = "Result"
    others="Others(Not_moved)"
    print(f'{message:*^30s}')
    for key,value in res.items():
        if key == others:
            continue
        print(f'{value} file moved into Category {os.path.join(RESULT_DIR,key)}')
    print(f'{res[others]} file Not moved')    
