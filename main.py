import os


def get_total_files(directory, level=0):
    """
    Returns total files in a folder.
    ---------
    Default to same folder without sub-directories.

    Arguments:
        directory:
        level: (default 0) change if you want to span all subdirectories
    """
    total_files = 0
    walk_path = os.walk(directory)
    for _, folder, files in walk_path:
        total_files += len(files)
        # print(files)
        if level == 0:
            break

    # print(total_files)
    return total_files


def main():
    total_files = get_total_files(path)
    print('total_files ->', total_files)


if __name__ == "__main__":
    path = 'C:/Users/Mayank/Documents/Sublime'
    main()
