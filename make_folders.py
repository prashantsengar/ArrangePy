import os


def makeFolders(root, lst):
    """
    Accept A List of Folder name and
    create that category name folder in RESULT_DIR
    """
    if os.path.exists(root) is False:
        os.mkdir(root)

    for name in lst:
        if name not in os.listdir(root):
            os.mkdir(os.path.join(root, name))
