:: Always run this directly from the ehealthkd-2019 folder, **not** from inside the `scripts` folder, like this:
:: $ scripts\run_baseline.bat

python -m scripts.baseline data\training\input_training.txt data\development\input_develop.txt data\submit\scenario1-main\output_scenario1.txt
python -m scripts.score data\development\input_develop.txt data\submit\scenario1-main\output_scenario1.txt

python -m scripts.baseline --skip-B data\training\input_training.txt data\development\input_develop.txt data\submit\scenario2-taskA\output_scenario2.txt
python -m scripts.score --skip-B data\development\input_develop.txt data\submit\scenario2-taskA\output_scenario2.txt

python -m scripts.baseline --skip-A data\training\input_training.txt data\development\input_develop.txt data\submit\scenario3-taskB\output_scenario3.txt
python -m scripts.score --skip-A data\development\input_develop.txt data\submit\scenario3-taskB\output_scenario3.txt
