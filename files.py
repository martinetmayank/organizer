import os
import shutil


def get_total_files(directory, level=0):
    """
    Returns total files in a folder.
    ---------
    Default to same folder without sub-directories.

    directory: the folder location.\n
    level: (default 0) change if you want to span all subdirectories
    """
    total_files = 0
    walk_path = os.walk(directory)
    for _, folder, files in walk_path:
        total_files += len(files)

        if level == 0:
            break

    return total_files


def get_file_list(directory, level=0):
    """
    Returns file list of a folder.
    ---------
    Default to same folder without sub-directories.

    directory: the folder location.\n
    level: (default 0) change if you want to span all subdirectories
    """
    walk_path = os.walk(directory)
    for _, folder, files in walk_path:
        return files


def move_files(source, target):
    """
    Move files to folder.
    ----------
    source: the file path.
    target: the target folder name.\n
    """
    shutil.move(source, target)
