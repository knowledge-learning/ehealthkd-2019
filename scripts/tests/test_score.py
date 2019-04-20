# coding: utf8

from pathlib import Path
from ..utils import Collection
from ..score import subtaskA, subtaskB


def load():
    gold = Collection()
    gold.load(Path(__file__).parent / "data" / "input_gold.txt" )

    submit = Collection()
    submit.load(Path(__file__).parent / "data" / "input_submit.txt" )

    return gold, submit

def test_task_A():
    gold, submit = load()
    dataA = subtaskA(gold, submit)

    assert len(dataA['correct_A']) == 3
    assert len(dataA['missing_A']) == 1
    assert dataA['missing_A'][0].id == 1


def test_task_B():
    gold, submit = load()
    dataA = subtaskA(gold, submit)
    dataB = subtaskB(gold, submit, dataA)

    assert len(dataB['correct_B']) == 2
    assert len(dataB['missing_B']) == 1
    assert dataB['missing_B'][0].label == 'same-as'

