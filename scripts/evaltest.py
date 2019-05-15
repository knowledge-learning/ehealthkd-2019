# coding: utf8

import collections
import argparse
import pprint
import json

from pathlib import Path
from .score import subtaskA, subtaskB, compute_metrics
from .utils import Collection


def evaluate_scenario(submit, gold, scenario):
    submit_input = submit / ("output_scenario%i.txt" % scenario)

    if not submit_input.exists():
        submit_input = submit / ("input_scenario%i.txt" % scenario)

    if not submit_input.exists():
        raise ValueError("Input file not found in '%s'" % submit)

    submit = Collection().load(submit_input)

    resultA = subtaskA(gold, submit)
    resultB = subtaskB(gold, submit, resultA)

    results = {}

    for k,v in list(resultA.items()) + list(resultB.items()):
        results[k] = len(v)

    metrics = compute_metrics(dict(resultA, **resultB), skipA=scenario==3, skipB=scenario==2)
    results.update(metrics)

    return results


def evaluate_one(submit: Path, scenario1_gold, scenario2_gold, scenario3_gold):
    scenario1_submit = submit / "scenario1-main"
    scenario2_submit = submit / "scenario2-taskA"
    scenario3_submit = submit / "scenario3-taskB"

    scenario1 = dict(evaluate_scenario(scenario1_submit, scenario1_gold, 1), submit=submit.name)
    scenario2 = dict(evaluate_scenario(scenario2_submit, scenario2_gold, 2), submit=submit.name)
    scenario3 = dict(evaluate_scenario(scenario3_submit, scenario3_gold, 3), submit=submit.name)

    return dict(submit=submit.name,
                scenario1=scenario1,
                scenario2=scenario2,
                scenario3=scenario3)


def main(submits:Path, gold:Path, best=False, single=False, csv=False, pretty=False, final=False):
    users = collections.defaultdict(list)

    if csv and not best:
        raise ValueError("Error: --csv implies --best")

    if final and (not csv or not best):
        raise ValueError("Error: --final implies --csv and --best")

    scenario1_gold = Collection().load(gold / "scenario1-main" / "input_scenario1.txt")
    scenario2_gold = Collection().load(gold / "scenario2-taskA" / "input_scenario2.txt")
    scenario3_gold = Collection().load(gold / "scenario3-taskB" / "input_scenario3.txt")

    if single:
        for subfolder in submits.iterdir():
            users[submits.name].append(evaluate_one(subfolder, scenario1_gold, scenario2_gold, scenario3_gold))
    else:
        for userfolder in submits.iterdir():
            for subfolder in userfolder.iterdir():
                users[userfolder.name].append(evaluate_one(subfolder, scenario1_gold, scenario2_gold, scenario3_gold))

    results = dict(users)

    if best:
        results = filter_best(results)

    if csv:
        import pandas as pd

        items = []

        for user, data in results.items():
            userdata = dict(name=user)

            for k, metrics in data.items():
                userdata.update({"%s-%s"%(k,m):v for m,v in metrics.items()})

            items.append(userdata)

        df = pd.DataFrame(items)
        df = df.set_index('name').sort_index().transpose()

        if final:
            df1 = df.transpose()[['scenario1-f1', 'scenario1-precision', 'scenario1-recall']]
            df1 = df1.sort_values('scenario1-f1', ascending=False).to_csv()

            df2 = df.transpose()[['scenario2-f1', 'scenario2-precision', 'scenario2-recall']]
            df2 = df2.sort_values('scenario2-f1', ascending=False).to_csv()

            df3 = df.transpose()[['scenario3-f1', 'scenario3-precision', 'scenario3-recall']]
            df3 = df3.sort_values('scenario3-f1', ascending=False).to_csv()

            print(df1)
            print(df2)
            print(df3)

        elif pretty:
            print(df.to_html())
        else:
            print(df.to_csv())

    else:
        print(json.dumps(results, indent=2 if pretty else None))


def filter_best(results):
    best = {}

    for user, submits in results.items():
        scenario1 = [entry['scenario1'] for entry in submits]
        scenario2 = [entry['scenario2'] for entry in submits]
        scenario3 = [entry['scenario3'] for entry in submits]

        best1 = max(scenario1, key=lambda d:d['f1'])
        best2 = max(scenario2, key=lambda d:d['f1'])
        best3 = max(scenario3, key=lambda d:d['f1'])

        best[user] = dict(scenario1=best1, scenario2=best2, scenario3=best3)

    return best


if __name__ == "__main__":
    parser = argparse.ArgumentParser("evaltest")
    parser.add_argument("submits", help="Path to the submissions folder. This is the folder of all participants, or, if --single is passed, directly the folder of one participant. Each participant's folder contains subfolders with submissions.")
    parser.add_argument("gold", help="Path to the gold folder, e.g. './data/testing.'")
    parser.add_argument("--best", action='store_true', help="Report only the best submission per scenario, otherwise all submissions are reported.")
    parser.add_argument("--single", action='store_true', help="If passed, then submits points to a single participant folder with submission folders inside, otherwise submits points to a folder with many participants, each with submission folders inside.")
    parser.add_argument("--csv", action='store_true', help="If passed then results are formatted as a table, can only be used with --best. Otherwise, results are returned in JSON format.")
    parser.add_argument("--pretty", action='store_true', help="If passed results are pretty printed: indented in JSON or in HTML when using --csv.")
    parser.add_argument("--final", action='store_true', help="If passed, results are formatted for final publication. Can only be passed with --csv and --best.")
    args = parser.parse_args()
    main(Path(args.submits), Path(args.gold), args.best, args.single, args.csv, args.pretty, args.final)

