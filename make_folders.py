import os


def makeFolders(root, lst):
    """
    Accept A List of Folder name and
    create that category name folder in RESULT_DIR
    """
    if os.path.exists(root) is False:
        os.mkdirs(root)

    for name in lst:
        if name not in os.listdir(root):
            os.mkdirs(os.path.join(root, name))
