import os
import sys
from collections import Counter, defaultdict, namedtuple


def find_duplicates(root_path):
    FileOnDisk = namedtuple("FileOnDisk", "name size")

    files = []
    filepaths_by_file = defaultdict(list)

    for dirpath, _, filenames in os.walk(root_path):
        for name in filenames:
            filepath = os.path.join(dirpath, name)
            file_on_disk = FileOnDisk(name, os.path.getsize(filepath))
            files.append(file_on_disk)
            filepaths_by_file[file_on_disk].append(filepath)

    file_counter = Counter(files)
    duplicates = filter(lambda item: item[1] > 1, file_counter.items())
    return {
        file_on_disk.name: filepaths_by_file[file_on_disk]
        for file_on_disk, _ in duplicates
    }


def print_duplicates(duplicates):
    for duplicate in duplicates.items():
        print(
            "File '{}' appears {} times:".format(
                duplicate[0], len(duplicate[1])
            )
        )
        for filepath in duplicate[1]:
            print("\t{}".format(filepath))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("No filename argument")

    root_path = sys.argv[1]
    if not os.path.exists(root_path):
        sys.exit("No such path")

    duplicates = find_duplicates(root_path)
    print_duplicates(duplicates)
