# coding: utf8

from score import *
from pathlib import Path

import warnings


def evaluate_scenario1(input_folder, output_folder):
    gold_input = Path(input_folder) / "ref" / "scenario1-main" / "input_scenario1.txt"
    gold = Collection()
    gold.load(gold_input)

    submit_input = Path(input_folder) / "res" / "scenario1-main" / "output_scenario1.txt"

    if not submit_input.exists():
        submit_input = Path(input_folder) / "res" / "scenario1-main" / "input_scenario1.txt"

    if not submit_input.exists():
        warnings.warn("It appears you did not submit for Scenario 1. If this is incorrect, please check the 3 output_* files in the `scenario1-main` folder.")

        return {
            'main_score': 0,
            'm_prec': 0,
            'm_rec': 0,
        }

    submit = Collection()
    submit.load(submit_input)

    data = OrderedDict()

    dataA = subtaskA(gold, submit, False)
    data.update(dataA)

    dataB = subtaskB(gold, submit, dataA, False)
    data.update(dataB)

    metrics = compute_metrics(data)

    return {
        'main_score': metrics['f1'],
        'm_prec': metrics['precision'],
        'm_rec': metrics['recall']
    }


def evaluate_scenario2(input_folder, output_folder):
    gold_input = Path(input_folder) / "ref" / "scenario2-taskA" / "input_scenario2.txt"
    gold = Collection()
    gold.load(gold_input)

    submit_input = Path(input_folder) / "res" / "scenario2-taskA" / "output_scenario2.txt"

    if not submit_input.exists():
        submit_input = Path(input_folder) / "res" / "scenario2-taskA" / "input_scenario2.txt"

    if not submit_input.exists():
        warnings.warn("It appears you did not submit for Scenario 2. If this is incorrect, please check the 3 output_* files in the `scenario2-taskA` folder.")

        return {
            'a_f1': 0,
            'a_prec': 0,
            'a_rec': 0,
        }

    submit = Collection()
    submit.load(submit_input)

    data = OrderedDict()

    dataA = subtaskA(gold, submit, False)
    data.update(dataA)

    metrics = compute_metrics(data, skipB=True)

    return {
        'a_f1': metrics['f1'],
        'a_prec': metrics['precision'],
        'a_rec': metrics['recall']
    }


def evaluate_scenario3(input_folder, output_folder):
    gold_input = Path(input_folder) / "ref" / "scenario3-taskB" / "input_scenario3.txt"
    gold = Collection()
    gold.load(gold_input)

    submit_input = Path(input_folder) / "res" / "scenario3-taskB" / "output_scenario3.txt"

    if not submit_input.exists():
        submit_input = Path(input_folder) / "res" / "scenario3-taskB" / "input_scenario3.txt"

    if not submit_input.exists():
        warnings.warn("It appears you did not submit for Scenario 3. If this is incorrect, please check the 3 output_* files in the `scenario2-taskB` folder.")

        return {
            'b_f1': 0,
            'b_prec': 0,
            'b_rec': 0,
        }

    submit = Collection()
    submit.load(submit_input)

    data = OrderedDict()

    dataA = subtaskA(gold, submit, False)
    data.update(dataA)

    dataB = subtaskB(gold, submit, dataA, False)
    data.update(dataB)

    metrics = compute_metrics(data, skipA=True)

    return {
        'b_f1': metrics['f1'],
        'b_prec': metrics['precision'],
        'b_rec': metrics['recall']
    }


def main(input_folder, output_folder):
    results = {}
    results.update(evaluate_scenario1(input_folder, output_folder))
    results.update(evaluate_scenario2(input_folder, output_folder))
    results.update(evaluate_scenario3(input_folder, output_folder))

    with (Path(output_folder) / "scores.txt").open("w") as fp:
        for key, value in results.items():
            fp.write("{}:{}\n".format(key, value))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('output')
    args = parser.parse_args()
    main(args.input, args.output)

