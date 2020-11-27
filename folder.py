import os
from pprint import pprint
from files import move_files, get_file_list, get_total_files


def get_total_folder(total_files, maximum_file):
    """
    Returns total folder that will be created.
    ----------
    total_files: total files in the folder.
    maximum_file: total files you want to keep in a folder.
    """
    total_folders = int(total_files / maximum_file) + 1
    print('Total folders that will be created:', total_folders)
    return total_folders


def create_folder(total_folders, name='folder', default_folder=None):
    """
    Creates the required folder.
    ----------

    total_folders: total number of folders that will be created.\n
    name: initital name of the folder.
    default_folder: (default None)
    """
    if default_folder is None:
        current_path = os.path.abspath(os.getcwd())
        print(current_path)
    else:
        current_path = default_folder

    organized_folder = current_path + "\\" + "sorted"
    os.mkdir(organized_folder)
    created_folders = list()
    for x in range(0, total_folders):
        folder_name = organized_folder + "\\" + name + ' 00' + str(x)
        os.mkdir(folder_name)
        created_folders.append(folder_name)

    return created_folders


def sort_folder(path, maximum_file=2):
    """
    The main function to sort folder.
    """
    total_files = get_total_files(path)
    file_list = get_file_list(path)
    total_folder = get_total_folder(total_files, maximum_file)
    folder_list = create_folder(total_folder)

    pprint(folder_list)
    return
    for folder in folder_list:
        for file in file_list:
            move_files(file, folder, maximum_file)
