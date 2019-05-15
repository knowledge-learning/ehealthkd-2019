# coding: utf8

import sys
from pathlib import Path
import random
from .utils import Collection, Sentence


def main(anns_path: Path, training_path, develop_path, test_path):
    collection = Collection()

    for file in sorted((anns_path / "traindev").iterdir()):
        if file.name.endswith('.txt'):
            collection.load_ann(file)

    for file in sorted((anns_path / "test").iterdir()):
        if file.name.endswith('.txt'):
            collection.load_ann(file)

    for file in sorted((anns_path / "trial").iterdir()):
        if file.name.endswith('.txt'):
            collection.load_ann(file)

    for s in collection.sentences:
        overlaps = s.overlapping_keyphrases()

        if overlaps:
            print("Found overlapping:", overlaps)
            s.merge_overlapping_keyphrases()
            overlaps = s.overlapping_keyphrases()

        dups = s.dup_relations()

        if dups:
            print("Found duplicated relations %r in sentence '%s'" % ([v[0] for v in dups.values()], s.text))
            s.remove_dup_relations()
            dups = s.dup_relations()

        assert not overlaps
        assert not dups

    current_sentences = set(s.text for s in collection.sentences)
    extra_sentences = []

    for file in sorted((anns_path / "plain").iterdir()):
        if file.name.endswith('.txt'):
            with file.open() as fp:
                file_sentences = [s.strip() for s in fp.read().split("\n") if s.strip()]

                for s in file_sentences:
                    if s not in current_sentences:
                        extra_sentences.append(s)

    random.seed(42)
    train_develop = collection.sentences[:700]
    random.shuffle(train_develop)

    training = Collection(train_develop[:600])
    develop = Collection(train_develop[600:])

    training.dump(training_path / "input_training.txt")
    develop.dump(develop_path / "input_develop.txt")

    test_sentences = collection.sentences[700:1000]
    random.shuffle(test_sentences)

    random.shuffle(extra_sentences)
    extra_sentences = [Sentence(s) for s in extra_sentences[:8700]]

    scn1 = Collection(extra_sentences[:3118] + test_sentences[:100] + extra_sentences[3118:])
    scn2 = Collection(test_sentences[100:200])
    scn3 = Collection(test_sentences[200:])

    print(len(scn1))

    scn1.dump(test_path / "scenario1-main" / "input_scenario1.txt", False)
    scn2.dump(test_path / "scenario2-taskA" / "input_scenario2.txt")
    scn3.dump(test_path / "scenario3-taskB" / "input_scenario3.txt")


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]), Path(sys.argv[4]))

