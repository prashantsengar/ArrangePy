import os
import shutil
import configparser
import re


def startProcess(folder, file, index, root_dst):
    """
    Accept file name and parent folder_name(folder)
    Return a Tuple(TRUE|FALSE,TYPE_OF_FILE)

    """
    src = os.path.join(folder, file)
    ext = os.path.splitext(file)[1].lower()
    dst_folder = identifyType(ext, index)
    if dst_folder is not None:
        dst = os.path.join(root_dst, dst_folder)
        return moveFiles(src, dst), dst_folder
    return False, "Others(Not_moved)"


def moveFiles(src, dst):
    """
    Accept source and destination and move files .
    Return True if File is Copied other wise False

    """
    try:
        shutil.move(src, dst)
        res = True
    except:
        res = False
    return res


def identifyType(ext, lst):
    """
    Accept extenssion Example .pdf .mp4 and
    return a category type from FOLDER_TYPES Dictionary

    """
    for (key, value) in lst.items():
        if ext[1:] in value:
            return key
    return None


def makeFolders(root, lst):
    """
    Accept A List of Folder name and
    create that category name folder in RESULT_DIR

    """
    if os.path.exists(root) is False:
        os.makedirs(root)
    print(os.path.abspath(root))

    for name in lst:
        if name not in os.listdir(root):
            os.makedirs(os.path.join(root, name))


def configure():
    """
    Read configuration file and create index of
    extentions with respect to their folder types

    """
    config = configparser.ConfigParser()
    config.read("config.ini")
    extension = config["ext"]
    p = re.compile(r"\'(.*?)\'")
    FOLDER_TYPES = {key: extension[key] for key in extension}
    for key in FOLDER_TYPES:
        FOLDER_TYPES[key] = p.findall(FOLDER_TYPES[key])

    return FOLDER_TYPES
