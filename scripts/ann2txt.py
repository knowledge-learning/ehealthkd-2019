# coding: utf8

import sys
from pathlib import Path
from .utils import Collection


def main(finput, foutput):
    collection = Collection()
    collection.load_ann(finput)
    collection.dump(foutput)


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]))
