import os
import shutil


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