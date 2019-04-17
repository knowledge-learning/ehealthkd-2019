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

Clone the `ehealthkd-2019` project from Github:

```bash
$ git clone https://github.com/knowledge-learning/ehealthkd-2019.git
```

Run the baseline implementation for the main scenario. The baseline implementation is in the `scripts/baseline.py` file. The arguments are:

* The path to the `input_training.txt`
* The path to the test file (in this case is the development file `input_develop.txt`)
* The path to the desired output file (`submit/scenario1-main/input_scenario1.txt`)

In this case we will train with the `training` set (600 sentences) and evaluate on the `development` set (100 sentences) using the same sentences for the 3 evaluation scenarios. However, in the final TEST phase you will train with both training and development and evaluate on the corresponding test sets (different for each scenario).

```bash
$ cd ehealthkd-2019
# Inside the root folder ehealthkd-2019
$ python3 scripts/baseline.py data/training/input_training.txt data/development/input_develop.txt data/submit/scenario1-main/input_scenario1.txt
```

Go to `data/submit/scenario1-main` and check the corresponding files were generated:

```bash
$ ls -l data/submit/scenario1-main
-rw-r--r-- 1 user user  8756 abr 17 19:01 input_scenario1.txt
-rw-r--r-- 1 user user 21604 abr 17 19:01 output_a_scenario1.txt
-rw-r--r-- 1 user user  1488 abr 17 19:01 output_b_scenario1.txt
```

> **(!!!)** Make sure that your files are named _exactly_ as the files above, since the evaluation script in Codalab will expect these filenames.

> **(!!!)** Also make sure that you have the file `input_scenario1.txt` with the input sentences in your submission folder. This is the _exact_ same file you processed as input, so you can just copy and paste it, but remember to _rename it_. The baseline script already handles this. This is necessary for the evaluation script to guarantee that you have the right sentences. 

Now you can run the evaluation script offline just to check your results. The evaluation script is in the file `scripts/score.py` and the arguments are:

* The gold annotations (in this case, `data/development/input_develop.txt`).
* Your system's annotations (`data/submit/scenario1-main/input_scenario1.txt`)

The evaluation script outputs the total number of correct, incorrect, partial, missing and spurious matches for each subtask, and the final score as defined in the [Evaluation section](/evaluation).

```bash
$ python3 scripts/score.py data/development/input_develop.txt data/submit/scenario1-main/input_scenario1.txt

correct_A: 366
incorrect_A: 42
partial_A: 33
spurious_A: 284
missing_A: 162
correct_B: 32
spurious_B: 66
missing_B: 391
--------------------
recall: 0.5036
precision: 0.404
f1: 0.4484
```

> **NOTE:** The exact numbers you see with the baseline may vary, as the evaluation script and/or the baseline implementation can suffer changes as we discover bugs or mistakes. These numbers are for illustrative purposes only. The actual scores are the ones published in Codalab.

You can pass `--verbose` if you want to see detailed information about which keyphrases and relations were correct, missing, etc.

```bash
$ python3 scripts/score.py --verbose data/development/input_develop.txt data/submit/scenario1-main/input_scenario1.txt 

===================  PARTIAL_A  ===================

Keyphrase(text='defecto', label='Concept', id=32) --> Keyphrase(text='defecto de nacimiento', label='Concept', id=30)
Keyphrase(text='aborto', label='Concept', id=39) --> Keyphrase(text='aborto espontáneo', label='Concept', id=31)
Keyphrase(text='menos', label='Predicate', id=66) --> Keyphrase(text='al menos', label='Predicate', id=61)

... LOTS OF OUTPUT

===================  MISSING_B  ===================

Relation(from='producen', to='proteínas', label='target')
Relation(from='proteínas', to='correctas', label='in-context')
Relation(from='producen', to='genes', label='subject')
Relation(from='producen', to='proteínas', label='target')
Relation(from='producen', to='correctamente', label='in-context')
Relation(from='trastorno', to='niño', label='target')
Relation(from='trastorno', to='genético', label='in-context')
--------------------
recall: 0.5036
precision: 0.404
f1: 0.4484
```

You can also (optionally) perform just subtask A or subtask B, writing the results to the corresponding folders.

For subtask A, the output folder is `submit/scenario2-taskA` and the dev file is `input_scenario2.txt`. Pass `--skip-B` to the baseline script to skip the output for subtask B. Again, we will be reusing the `development` set in this case, but in the TEST phase there will be an additional 100 sentences just for this scenario.

```bash
$ python3 scripts/baseline.py --skip-B data/training/input_training.txt data/development/input_develop.txt data/submit/scenario2-taskA/input_scenario2.txt
```

> **(!!!)** When submitting to subtask A, please make sure to write an **empty `output_b_scenario2.txt`** file. This file will not be taken into consideration when evaluating this scenario but is necessary for the evluation script when it parses the results. The baseline implementation already takes care of this detail.

You can evaluate just scenario 2 with the evaluation script by passing `--skip-B`:

```bash
$ python3 scripts/score.py --skip-B data/development/input_develop.txt data/submit/scenario2-taskA/input_scenario2.txt 

correct_A: 366
incorrect_A: 42
partial_A: 33
spurious_A: 284
missing_A: 162
--------------------
recall: 0.5276
precision: 0.6343
f1: 0.5761
```

For subtask B, the output folder is `submit/scenario3-taskB` and the dev file is `input_scenario3.txt`. Pass `--skip-A` to the baseline script to skip the output for subtask B. Again, we will be reusing the `development` set in this case, but in the TEST phase there will be an additional 100 sentences just for this scenario.

```bash
$ python3 scripts/baseline.py --skip-A data/training/input_training.txt data/development/input_develop.txt data/submit/scenario3-taskB/input_scenario3.txt
```

> **(!!!)** When submitting to subtask B, please make sure to **copy the `output_a_scenario3.txt`** file _from the gold annotations_. This is the same as the `output_a_develop.txt` file in this case. This file will not be taken into consideration when evaluating this scenario but is necessary for the evaluation script when it parses the results. The baseline implementation already takes care of this detail.

> **(!!!)** When submitting to subtask B, make sure to **reuse the keyphrase ID** provided in the `output_a_develop.txt` (or corresponding TEST file) from the gold annotations. The baseline implementation already takes care of this detail.

You can evaluate just scenario 2 with the evaluation script by passing `--skip-A`:

```bash
$ python3 scripts/score.py --skip-A data/development/input_develop.txt data/submit/scenario3-taskB/input_scenario3.txt 

correct_B: 36
spurious_B: 14
missing_B: 387
--------------------
recall: 0.72
precision: 0.08511
f1: 0.1522
```

If you have succesfully generated the output files for all the scenarios, you should have the following structure in the `data/submit` folder:

```bash
$ ls -lR data/submit
data/submit:
total 16
-rw-r--r-- 1 user user  762 abr 17 19:06 Readme.md
drwxr-xr-x 2 user user 4096 abr 17 19:01 scenario1-main
drwxr-xr-x 2 user user 4096 abr 17 19:01 scenario2-taskA
drwxr-xr-x 2 user user 4096 abr 17 19:02 scenario3-taskB

data/submit/scenario1-main:
total 40
-rw-r--r-- 1 user user  8756 abr 17 19:01 input_scenario1.txt
-rw-r--r-- 1 user user 21604 abr 17 19:01 output_a_scenario1.txt
-rw-r--r-- 1 user user  1488 abr 17 19:01 output_b_scenario1.txt

data/submit/scenario2-taskA:
total 36
-rw-r--r-- 1 user user  8756 abr 17 19:38 input_scenario2.txt
-rw-r--r-- 1 user user 21604 abr 17 19:38 output_a_scenario2.txt
-rw-r--r-- 1 user user     0 abr 17 19:38 output_b_scenario2.txt

data/submit/scenario3-taskB:
total 36
-rw-r--r-- 1 user user  8756 abr 17 19:46 input_scenario3.txt
-rw-r--r-- 1 user user 19744 abr 17 19:46 output_a_scenario3.txt
-rw-r--r-- 1 user user   764 abr 17 19:46 output_b_scenario3.txt
```

> **(!!!)** Please double-check the files for all three scenarios, including the empty `output_b_scenario2.txt` and the copied `output_a_scenario3.txt`. If you do not plan to participate in any given scenario, kindly reuse the baseline output then, to avoid the evaluation script from raising errors about missing files.

## Submitting your results to Codalab

Once you have all the corresponding outputs, please bundle the content of the submit folder in a `.zip` file:

```bash
$ cd data/submit
$ zip -r submit.zip *
```

> **(!!!)** Make sure you zip **the content** of the `submit` folder, and not the `submit` _itself_. When in doubt, `cd` into `data/submit` and run `zip` there. The idea is that the root of your `submit.zip` file should directly contain the three folders `scenario1-main`, etc., and **not** a `submit` folder. 

Go to the [Codalab competition page](https://competitions.codalab.org/competitions/21781) and register if you have not done so already.

Please also make sure to fill-in this [Google Form](https://forms.gle/3KHAvo7e5MfxtnME9) to accept the license terms for the corpus.

In Codalab, go to the [Participate](https://competitions.codalab.org/competitions/21781#participate-submit_results) section and enter the details of your submission:

In the submission page (below) please fill in the following information:

* Team name.
Method name: a short, memorable name for the technique you are * presenting.
* Method description: refers to the type of techniques used. Please write a summary (~200 words) of the techniques, algorithms or approaches used. Also specify if you use external sources (other corpora, knowledge bases, etc.). 
Finally, attach one or more of the following tags regarding techniques and/or resources used in your approach. These tags will help us better understand which approaches are more popular or perform better in this task in the future.

    * K: knowledge-bases
    * S: Shallow supervised methods (i.e., logistic regression, SVM, Markov models, CRF, ...)
    * D: Deep supervised methods (e.g, CNNs, LSTMs, ...)
    * U: Unsupervised methods (e.g. clustering or dimensionality reduction techniques, ...)
    * E: Embeddings (e.g., word2vec, BERT, ELMo, ...)
    * N: Standard NLP techniques (pos-tagging, AMR parsing, dependency parsing, NER, ...)
    * R: Hand-crafted rules

Finally hit the submit button and attach you zip file. If everything is ok, after a few seconds hit the **Submit to leaderboard** button at the bottom of the page to see your results.

> **DISCLAIMER:** The scoring you achieve during the training phase is only for your own reference, and should not be taken as an indication that you will achieve a similar score in the test phase. Particularly, participants that achieve the highest scores in the training phase are **not guaranteed** to win in the TEST phase, since participating in the training phase is completely optional. Likewise, at any point we may decide to change the evaluation script, including during the blind TEST phase, if we discover any kind of bug or error. We will inform if that's the case and provide an updated evaluation script.

Finally, if you discover a mistake in the evaluation script, please let us know at [ehealth-kd@googlegroups.com](mailto:ehealth-kd@googlegroups.com) or post an issue on our [Issues Page](https://github.com/knowledge-learning/ehealthkd-v2/issues) in Github.
