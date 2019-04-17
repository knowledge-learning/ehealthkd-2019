---
title: Submission
permalink: /submission
nav_order: 4
---

# Submission details

The challenge will be graded on [Codalab](https://competitions.codalab.org/competitions/21781).

A fully working [evaluation script](https://github.com/knowledge-learning/ehealthkd-2019/blob/master/scripts/score.py) is provided to participants, that exactly matches the evaluation formulas used in Codalab.
This way participants will have the possibility to evaluate their systems offline and perform hyper-parameter tuning with respect to the same evaluation metrics as used in the competition.

## Baseline implementation

A [baseline system](https://github.com/knowledge-learning/ehealthkd-2019/blob/master/scripts/baseline.py) is provided for participants to compare their results. If necessary, feel free to use the baseline as a starting point for developing your own solution, since the baseline already covers parsing the input and generating output in the correct format.

The baseline implementation is an extremely basic strategy that simply stores all the training, and at test time outputs keyphrases and relations if they exactly match something found in the training.

We recommend all participants to first run the baseline implementation (with the training and development sets) and upload it to Codalab, to get acquainted with the submission process. The following instructions detail this process.

## Running the baseline implementation on the development set

The first step consists in downloading the project and running the baseline implementation.

1. Clone the `ehealthkd-2019` project from Github:

```bash
$ git clone https://github.com/knowledge-learning/ehealthkd-2019.git
$ cd ehealthkd-2019
```

2. Run the baseline implementation for the main scenario. The baseline implementation is in the `scripts/baseline.py` file. The arguments are:

    * The path to the `input_training.txt`
    * The path to the test file (in this case is the development file `input_develop.txt`)
    * The path to the desired output file (`submit/scenario1-main/input.txt`)

```bash
# Inside the root folder ehealthkd-2019
$ python3 scripts/baseline.py data/training/input_training.txt data/development/input_develop.txt data/submit/scenario1-main/input.txt
```

3. Go to `data/submit/scenario1-main` and check the output files were generated:

```bash
$ ls -l data/submit/scenario1-main
-rw-rw-r-- 1 user user  8756 abr 17 17:24 input.txt
-rw-rw-r-- 1 user user 21604 abr 17 17:24 output_a_txt
-rw-rw-r-- 1 user user  1485 abr 17 17:24 output_b_txt
```

4.
