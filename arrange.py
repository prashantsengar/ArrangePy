# arrange.py
# Arranges the fiels according to their types for later classification

import os
import sys
import shutil
import configparser
import re
import sys
import time

'''
Read Configuration file for Extensions using RegEx
'''
config=configparser.ConfigParser()
config.read('config.ini')
extension=config['ext']

# RegEX reading of config file for faster execution
p = re.compile(r'\'(.*?)\'')
FOLDER_TYPES = {key:extension[key] for key in extension}
for key in FOLDER_TYPES:
    FOLDER_TYPES[key] = p.findall(FOLDER_TYPES[key])

'''
Takes Command Line Argument for File Location.
Defaults to Current location if not specified
'''
RESULT_DIR = 'CleanedPy'
try:
    RESULT_DIR = os.path.join(sys.argv[1],RESULT_DIR)
except:
    pass

def identifyType(ext):
    '''
    Accept extenssion Example .pdf .mp4 and
    return a category type from FOLDER_TYPES Dictionary
    '''
    for key,value in FOLDER_TYPES.items():
        if ext[1:] in value:
            return key
    else:
        return None


def makeFolders(lst):
    '''
    Accept A List of Folder name and
    create that category name folder in RESULT_DIR
    '''
    if os.path.exists(RESULT_DIR) is False:
        os.mkdir(RESULT_DIR)
                      
    for name in lst:
        if name not in os.listdir(RESULT_DIR):
            os.mkdir(os.path.join(RESULT_DIR,name))

def moveFiles(src,dst):
    '''
    Accept source and destination and move files .
    Return True if File is Copied other wise False
    '''
    res = True
    try:
        shutil.move(src,os.path.join(RESULT_DIR,dst))
    except:
        res = False
    return res

# Create Output and category folder if not Exists
makeFolders(FOLDER_TYPES.keys())

def startProcess(folder,file):
    '''
    Accept file name and parent folder_name(folder)
    Return a Tuple(TRUE|FALSE,TYPE_OF_FILE)
    
    '''
    types = os.path.splitext(file)[1].lower()
    src = os.path.join(folder,file)
    dst = identifyType(types)
    if dst is not None:
        return moveFiles(src,dst),dst
    return False,'Others(Not_moved)'

def strong_arrange(warn=True):
    if warn == True:
        print("You are going to strong arrange ",
              "the directory DIRECTORY_NAME. ",
              "It will rearrange all the files ",
              "in the subfolders as well. ", 
              "It might cause issues if you ",
              "have added wrong extensions ",
              "in the config.ini file and run ",
              "the program in a sensitive directory. ",
              "You still have 5 seconds to ",
              "cancel it if you want to review anything. ",
              "(Press Ctrl+C to abort)")
        try:
            time.sleep(5)
        except KeyboardInterrupt:
            sys.exit()        
    TOTAL_COUNT={}
    for foldername, subfolders, filenames in os.walk(folder):
        for file in filenames:
            if os.path.isfile(os.path.join(folder,file)):
               status,types = startProcess(folder,file)
               if types in TOTAL_COUNT:
                   TOTAL_COUNT[types] = TOTAL_COUNT[types]+1
               else:
                   TOTAL_COUNT[types] = 1
    return TOTAL_COUNT
  
def arrange():
    TOTAL_COUNT = {}
    for file in os.listdir(folder):
        if os.path.isfile(os.path.join(folder,file)):
            status,types = startProcess(folder,file)
            if types in TOTAL_COUNT:
                TOTAL_COUNT[types] = TOTAL_COUNT[types]+1
            else:
                TOTAL_COUNT[types]=1
    return TOTAL_COUNT

if __name__ == '__main__':

    print("Arrange files")
    try:
        folder = sys.argv[1]
    except:
        folder = os.getcwd()
    print(folder)

    choice = int(input("Press 1 for Weak arrange\nPress 2 for Strong arrange\n0 to exit\noption:"))

    if choice == 1:
        res = arrange()
    if choice == 2:
        res = strong_arrange()
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
