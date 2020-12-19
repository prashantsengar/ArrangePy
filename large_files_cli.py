import os
import time
import argparse


class file_data:
    def __init__(self):
        self.name = os.getcwd()
        self.size = 0.0
        self.ext = "B"

    def __lt__(self, other):
        return self.size > other.size


def walk_dir(path):
    file_lst = []
    for folderName, sub_folders, filenames in os.walk(path):
        for filename in filenames:
            pt = file_data()
            pt.name = os.path.join(folderName, filename)
            ext = os.stat(pt.name)
            pt.size = ext.st_size
            file_lst.append(pt)
    return file_lst


def sort_and_normalize_and_save(initial_list, save_data):
    initial_list.sort()
    extensions = ["B", "KB", "MB", "GB", "TB"]
    p = 0
    file = open(save_data, "w")
    string = "Name,Size,Units\n"
    for element in initial_list:
        i = 0
        p += element.size
        while element.size > 1024.0:
            element.size = element.size / 1024
            i += 1
        element.size = round(element.size, 3)
        element.ext = extensions[i]
        string += f"{element.name},{element.size},{element.ext}\n"
    file.write(string)
    file.close()
    print(f"Data has been saved to the file {save_data}.")


def main():
    my_parser = argparse.ArgumentParser(description='List the content of a folder')

    # Add the arguments
    my_parser.add_argument('Path',
                           metavar='path',
                           type=str,
                           help='the path to list')

    args = my_parser.parse_args()
    input_path = args.Path
    if os.path.isdir(input_path):
        lst = walk_dir(input_path)
        start = time.time()
        file_name = "data.csv"
        sort_and_normalize_and_save(lst, file_name)
        print("Time taken: ", time.time() - start, "sec")
    else:
        print("Invalid path specified")


main()
