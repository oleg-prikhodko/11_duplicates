import os
import sys
from collections import Counter, defaultdict, namedtuple
from pprint import pprint


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


if __name__ == "__main__":
    pprint(find_duplicates(sys.argv[1]))
