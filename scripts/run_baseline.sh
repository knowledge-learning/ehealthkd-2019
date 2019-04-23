#!/bin/sh

# Always run this directly from the ehealthkd-2019 folder, **not** from inside the `scripts` folder, like this:
# $ ./scripts/run_baseline.sh

echo "\nMain Scenario\n*************"
python3 -m scripts.baseline data/training/input_training.txt data/development/input_develop.txt data/submit/scenario1-main/output_scenario1.txt
python3 -m scripts.score data/development/input_develop.txt data/submit/scenario1-main/output_scenario1.txt

echo "\nOptional Scenario A\n*******************"
python3 -m scripts.baseline --skip-B data/training/input_training.txt data/development/input_develop.txt data/submit/scenario2-taskA/output_scenario2.txt
python3 -m scripts.score --skip-B data/development/input_develop.txt data/submit/scenario2-taskA/output_scenario2.txt

echo "\nOptional Scenario B\n*******************"
python3 -m scripts.baseline --skip-A data/training/input_training.txt data/development/input_develop.txt data/submit/scenario3-taskB/output_scenario3.txt
python3 -m scripts.score --skip-A data/development/input_develop.txt data/submit/scenario3-taskB/output_scenario3.txt

echo "\nZipping\n*********"
cd data/submit && zip -r submit.zip scenario1-main scenario2-taskA scenario3-taskB

