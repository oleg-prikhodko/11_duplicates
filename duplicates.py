import os
import sys
from collections import defaultdict, namedtuple


# Дубликаты – это два файла с одинаковым именем и размером.
FileOnDisk = namedtuple("FileOnDisk", "name size")


def find_duplicates(root_path):
    filepaths_by_files = defaultdict(list)

    for dirpath, _, filenames in os.walk(root_path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            file_on_disk = FileOnDisk(filename, os.path.getsize(filepath))
            filepaths_by_files[file_on_disk].append(filepath)

    duplicates = dict(
        filter(
            lambda filepaths_by_file: len(filepaths_by_file[1]) > 1,
            filepaths_by_files.items(),
        )
    )
    return duplicates


def print_duplicates(duplicates):
    for file_on_disk, filepaths in duplicates.items():
        print(
            "File '{}' appears {} times:".format(
                file_on_disk.name, len(filepaths)
            )
        )
        for filepath in filepaths:
            print("\t{}".format(filepath))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("No filename argument")

    root_path = sys.argv[1]
    if not os.path.exists(root_path) or not os.path.isdir(root_path):
        sys.exit("Input path is incorrect")

    duplicates = find_duplicates(root_path)
    if not duplicates:
        print("No duplicates found")
    else:
        print_duplicates(duplicates)
