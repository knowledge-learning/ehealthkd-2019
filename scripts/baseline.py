# coding: utf8

import argparse
import re
import sys
from pathlib import Path

from .utils import Collection, Keyphrase, Relation, Sentence


def train(finput: Path):
    doc = Collection()
    doc.load(finput)

    keyphrases = {}
    for sentence in doc.sentences:
        for keyphrase in sentence.keyphrases:
            text = keyphrase.text.lower()
            keyphrases[text] = keyphrase.label

    relations = {}
    for sentence in doc.sentences:
        for relation in sentence.relations:
            origin = relation.from_phrase
            origin_text = origin.text.lower()
            destination = relation.to_phrase
            destination_text = destination.text.lower()

            relations[origin_text, origin.label, destination_text, destination.label] = relation.label

    return keyphrases, relations

def test(finput: Path, model, skip_A, skip_B):
    doc = Collection()
    gold_keyphrases, gold_relations = model

    if skip_A:
        doc.load_keyphrases(finput)
    else:
        doc.load_input(finput)
        next_id = 0
        for gold_keyphrase, label in gold_keyphrases.items():
            for sentence in doc.sentences:
                text = sentence.text.lower()
                pattern = r'\b' + gold_keyphrase + r'\b'
                for match in re.finditer(pattern, text):
                    keyphrase = Keyphrase(sentence, label, next_id, [match.span()])
                    keyphrase.split()
                    next_id += 1

                    sentence.keyphrases.append(keyphrase)

    if not skip_B:
        for sentence in doc.sentences:
            for origin in sentence.keyphrases:
                origin_text = origin.text.lower()
                for destination in sentence.keyphrases:
                    destination_text = destination.text.lower()
                    try:
                        label = gold_relations[origin_text, origin.label, destination_text, destination.label]
                    except KeyError:
                        continue
                    relation = Relation(sentence, origin.id, destination.id, label)
                    sentence.relations.append(relation)

            sentence.remove_dup_relations()

    return doc

def main(training_input, testing_input, foutput, skip_A, skip_B):
    model = train(training_input)
    doc = test(testing_input, model, skip_A, skip_B)
    doc.dump(foutput, skip_empty_sentences=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('training')
    parser.add_argument('test')
    parser.add_argument('output')
    parser.add_argument('--skip-A', action='store_true')
    parser.add_argument('--skip-B', action='store_true')
    args = parser.parse_args()
    main(Path(args.training), Path(args.test), Path(args.output), args.skip_A, args.skip_B)
