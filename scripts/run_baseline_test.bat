:: Always run this directly from the ehealthkd-2019 folder, **not** from inside the `scripts` folder, like this:
:: $ scripts\run_baseline.bat

python -m scripts.baseline data\training\input_training.txt data\testing\scenario1-main\input_scenario1.txt data\submit\scenario1-main\output_scenario1.txt

python -m scripts.baseline --skip-B data\training\input_training.txt data\testing\scenario2-taskA\input_scenario2.txt data\submit\scenario2-taskA\output_scenario2.txt

python -m scripts.baseline --skip-A data\training\input_training.txt data\testing\scenario3-taskB\input_scenario3.txt data\submit\scenario3-taskB\output_scenario3.txt

