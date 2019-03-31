# coding: utf8

import sys
from pathlib import Path
from utils import Collection
import random


def main(anns_path: Path, training_path, develop_path):
    collection = Collection()

    for file in sorted(anns_path.iterdir()):
        if file.name.endswith('.txt'):
            collection.load_ann(file)

    for s in collection.sentences:
        overlaps = s.overlapping_keyphrases()

        if overlaps:
            print("Found overlapping:", overlaps)

            s.merge_overlapping_keyphrases()

            overlaps = s.overlapping_keyphrases()

        assert not overlaps

    random.seed(42)
    train_develop = collection.sentences[:700]
    random.shuffle(train_develop)

    training = Collection(train_develop[:600])
    develop = Collection(train_develop[600:])

    training.dump(training_path / "input_training.txt")
    develop.dump(develop_path / "input_develop.txt")


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]))

