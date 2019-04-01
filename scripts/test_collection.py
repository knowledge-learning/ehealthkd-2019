# coding: utf8

import sys
from pathlib import Path
from utils import Collection


def main(path):
    collection = Collection()
    collection.load(path)

    for sentence in collection.sentences:
        print(sentence)


if __name__ == "__main__":
    main(Path(sys.argv[1]))

