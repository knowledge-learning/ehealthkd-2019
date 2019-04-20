# coding: utf8

from pathlib import Path
from ..utils import Collection


def test_parse():
    collection = Collection()
    collection.load(Path(__file__).parent / "data" / "input_gold.txt" )

    assert len(collection.sentences) == 1

    s = collection.sentences[0]

    assert len(s.keyphrases) == 4
    assert len(s.relations) == 3

