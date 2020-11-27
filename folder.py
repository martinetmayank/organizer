import os
from files import move_files, get_file_list, get_total_files
import shutil


def get_total_folder(total_files, maximum_file):
    """
    Returns total folder that will be created.
    ----------

    total_files: total files in the folder.\n
    maximum_file: total files you want to keep in a folder.
    """

    total_folders = (total_files / maximum_file)

    if int(total_folders) < total_folders:
        total_folders = int(total_folders) + 1

    print('Total folders that will be created:', total_folders)
    return total_folders


def create_folder(total_folders, name='folder', default_folder=None):
    """
    Creates the required folder.
    ----------

    total_folders: total number of folders that will be created.\n
    name: initital name of the folder.\n
    default_folder: (default None)
    """

    if default_folder is None:
        current_path = os.path.abspath(os.getcwd())
    else:
        current_path = default_folder

    organized_folder = current_path + "\\" + "sorted"

    try:
        shutil.rmtree(organized_folder)
    except FileNotFoundError:
        pass

    os.mkdir(organized_folder)

    created_folders = list()
    for x in range(0, total_folders):
        folder_name = organized_folder + "\\" + name + ' 00' + str(x) + "\\"
        os.mkdir(folder_name)
        created_folders.append(folder_name)

    return created_folders


def sort_folder(path, maximum_file=50):
    """
    Function to sort folder.
    ------------------

    path: the folder location path.\n
    maximum_files: (default 50) maximum files to keep in a folder.
    """

    total_files = get_total_files(path)
    file_list = get_file_list(path)
    total_folder = get_total_folder(total_files, maximum_file)
    folder_list = create_folder(total_folder)

    file_counter = 0
    folder_counter = 0
    files_moved = 0

    while file_counter < len(file_list):
        file = path + "\\" + file_list[file_counter]
        move_files(file, folder_list[folder_counter])

        files_moved += 1
        if files_moved == maximum_file:
            folder_counter += 1
            files_moved = 0

        file_counter += 1

    return
