#!/bin/sh

# Always run this directly from the ehealthkd-2019 folder, **not** from inside the `scripts` folder, like this:
# $ ./scripts/run_baseline.sh

echo "\nMain Scenario\n*************"
python3 -m scripts.baseline data/training/input_training.txt data/testing/scenario1-main/input_scenario1.txt data/submit/scenario1-main/output_scenario1.txt

echo "\nOptional Scenario A\n*******************"
python3 -m scripts.baseline --skip-B data/training/input_training.txt data/testing/scenario2-taskA/input_scenario2.txt data/submit/scenario2-taskA/output_scenario2.txt

echo "\nOptional Scenario B\n*******************"
python3 -m scripts.baseline --skip-A data/training/input_training.txt data/testing/scenario3-taskB/input_scenario3.txt data/submit/scenario3-taskB/output_scenario3.txt

echo "\nZipping\n*********"
cd data/submit && zip -r submit.zip scenario1-main scenario2-taskA scenario3-taskB

