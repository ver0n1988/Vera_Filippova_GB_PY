import os
import sys

stats = {}


def get_memory(path):
     with os.scandir(path) as files:
        for f in files:
            if os.path.isfile(f):
                mem = 10 ** len(str(os.stat(f).st_size))
                stats[mem] = stats.get(mem, 0) + 1
            elif os.path.isdir(f):
                get_memory(os.path.join(path, f))


if __name__ == "__main__":

    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        path = os.getcwd()

    get_memory(path)
    print(stats)