# coding: utf8

import sys
from pathlib import Path
from utils import Collection
import random


def main(anns_path: Path):
    collection = Collection()

    for file in anns_path.iterdir():
        if file.name.endswith('.txt'):
            collection.load_ann(file)

    print(len(collection.sentences))




if __name__ == "__main__":
    main(Path(sys.argv[1]))

