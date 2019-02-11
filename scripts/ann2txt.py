# coding: utf8

import sys
from pathlib import Path
from utils import Collection


def main(finput):
    collection = Collection()
    collection.load_ann(finput)
    collection.dump(finput)


if __name__ == "__main__":
    main(Path(sys.argv[1]))
