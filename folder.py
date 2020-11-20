import os
import subprocess

from files import move_files, get_file_list


def get_total_folder(files, maximum=100):
    """
    Returns total folder that will be created.
    ----------
    Arguments:\n
        files: total files in the folder.
        maximum: total files you want to keep in a folder.
    """
    total_folders = int(files / maximum) + 1
    print('Total folders that will be created:', total_folders)
    return total_folders


def create_folder(folders, name='folder'):
    """
    Creates the required folder.
    ----------
    Arguments:\n
        folders: total folders that will be created.
        name: initital name of the folder.
    """
    current_path = os.path.abspath(os.getcwd())

    for x in range(0, folders):
        folder_name = current_path + "\\" + name + ' 00' + str(x)
        os.mkdir(folder_name)


def sort_folder(file_list, maximum=100):
    """
    The main function to sort folder.
    """
