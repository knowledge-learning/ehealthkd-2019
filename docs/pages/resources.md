---
title: Resources
permalink: /resources
nav_order: 5
---

# Linguistic resources

As in the previous edition, the corpus for eHealth-KD 2019 will be extracted from MedlinePlus sources.
This platform freely provides large health textual data from which we have made a selection for constituting the eHealth-KD corpus. The selection has been made by sampling specific XML files from the collection available in the [Medline website](https://medlineplus.gov/xml.html).

> "MedlinePlus is the National Institutes of Health's Website for patients and their families and friends. Produced by the National Library of Medicine, the world’s largest medical library, it brings you information about diseases, conditions, and wellness issues in language you can understand. MedlinePlus offers reliable, up-to-date health information, anytime, anywhere, for free." [1]

These files contain several entries related to health and medicine topics and have been processed to remove all XML markup to extract the textual content. Only Spanish language items were considered. Once cleaned, each individual item was converted to a plain text document, and some further post-processing is applied to remove unwanted sentences, such as headers, footers and similar elements, and to flatten HTML lists into plain sentences. The final documents are manually tagged using Brat by a group of annotators. After tagging, a post-processing was applied to Brat’s output files (ANN format) to obtain the output files in the formats described in this document.

> **NOTE:** The resulting documents and output files are distributed along with the Task. There is no need for participants to download extra data from MedlinePlus servers, since all the input is already distributed.

## Corpus data

The corpus will be divided into three sections. Training and development sets will be published along with baseline implementations, for participants to train and fine-tune their systems. These files will consist of both plain text input and the expected outputs for both subtasks. Afterward, a small test set will be released, with plain text only, further divided into 3 sub-sets, one for each scenario. Participants are expected to submit the corresponding output files to Codalab.

In no case, participants will be able to access the correct output files for the test set before the challenge ends. Afterward, the full corpus, including Brat-annotated files will be freely available under a suitable license for the research community.

### Download links:

All data is available in the [Github repository](https://github.com/knowledge-learning/ehealthkd-2019) of the project. Individual download links are listed below for ease of use.

### Trial data

* [Trial - raw input text](https://raw.githubusercontent.com/knowledge-learning/ehealthkd-2019/master/data/trial/input_trial.txt)
* [Trial - output for Subtask A](https://raw.githubusercontent.com/knowledge-learning/ehealthkd-2019/master/data/trial/output_a_trial.txt)
* [Trial - output for Subtask B](https://raw.githubusercontent.com/knowledge-learning/ehealthkd-2019/master/data/trial/output_b_trial.txt)

### Training and development

The eHealth-KD Corpus is distributed free of charge under a Creative Commons Non-Commercial Share-Alike 4.0 License.

To accept the distribution terms, please fill in the following form:
> [https://forms.gle/3KHAvo7e5MfxtnME9](https://forms.gle/3KHAvo7e5MfxtnME9)

The training set contains a total of 600 sentences manually annotated in [Brat](http://brat.nlplab.org/) and post-processed to match the input format.
These sentences are expected to be used for training machine learning systems.
An additional 100 sentences are available in the development set.
These additional sentences are expected to be used for evaluating machine learning systems and tune their hyperparameters.

### Test data

Now that the challenge has finished the full test set is released. The input files are:

* [Scenario 1 - raw input text](https://raw.githubusercontent.com/knowledge-learning/ehealthkd-2019/master/data/testing/scenario1-main/input_scenario1.txt)
* [Scenario 2 - raw input text](https://raw.githubusercontent.com/knowledge-learning/ehealthkd-2019/master/data/testing/scenario2-taskA/input_scenario2.txt)
* [Scenario 3 - raw input text](https://raw.githubusercontent.com/knowledge-learning/ehealthkd-2019/master/data/testing/scenario3-taskB/input_scenario3.txt)
* [Scenario 3 - output from subtask A](https://raw.githubusercontent.com/knowledge-learning/ehealthkd-2019/master/data/testing/scenario3-taskB/output_a_scenario3.txt)

The remaining gold files are:

* [Scenario 1 - output from subtaskA](https://raw.githubusercontent.com/knowledge-learning/ehealthkd-2019/master/data/testing/scenario1-main/output_a_scenario1.txt)
* [Scenario 1 - output from subtaskB](https://raw.githubusercontent.com/knowledge-learning/ehealthkd-2019/master/data/testing/scenario1-main/output_b_scenario1.txt)
* [Scenario 2 - output from subtaskA](https://raw.githubusercontent.com/knowledge-learning/ehealthkd-2019/master/data/testing/scenario2-taskA/input_a_scenario2.txt)
* [Scenario 2 - output from subtaskB](https://raw.githubusercontent.com/knowledge-learning/ehealthkd-2019/master/data/testing/scenario2-taskA/input_b_scenario2.txt)
* [Scenario 3 - output from subtaskB](https://raw.githubusercontent.com/knowledge-learning/ehealthkd-2019/master/data/testing/scenario3-taskB/output_b_scenario3.txt)


For scenario 1, a total of **8800 sentences** have been published. Of these, only 100 sentences will actually be evaluated, but you are required to submit the output _for the full set of 8800 sentences_, since the actual 100 sentences are randomly shuffled inside the 8800 set. This is done with the purpose to discourage participants from manually revising the test set and hand tunning their results. Furthermore, the remaining 8700 sentences annotated and submitted by participants will be published as an additional automatically labeled training set.

For scenarios 2 and 3, only the 100 valid sentences are published. In scenario 3 also the gold annotations for subtask A are provided, so that participants can focus only on subtask A. Details for the submission format are available in the [Submission section](submission).

## Evaluation scripts

Evaluation scripts will be provided so that participants can test offline their systems with respect to the same metrics used in the challenge. Since participants will not have access to the test gold annotations, their offline performance will need to be evaluated in the development set. This metric will not be exactly the same as the one obtained in the test set, but it should serve for participants to compare different strategies and perform hyper-parameter tunning.

### **Download links**:

The evaluation is available in the [Github repository](https://github.com/knowledge-learning/ehealthkd-2019) of the project, in the file `script/score.py`.
A detailed explanation is available in the [Submission section](/submission).

## Baselines

A simple baseline will be released along with the corpus. The baseline source code will be freely available as well. The baselines performance on the development and the test set will be published.

### **Download links**:

The evaluation is available in the [Github repository](https://github.com/knowledge-learning/ehealthkd-2019) of the project, in the file `script/baseline.py`.
A detailed explanation is available in the [Submission section](/submission).

# Additional resources

Participants may freely use any additional resources they consider necessary to improve their systems, from other corpora (annotated or not), to external knowledge either explicitly (i.e., using knowledge bases) or implicitly (i.e., captured in word embeddings). For the purpose of sharing the results we expect participants to fully disclose everything they use.
However, participants may not manually annotate the test set, since doing so would be in violation of the ethics of the competition. Furthermore, we expect participants to perform all the fine tuning using only the training and development, and then perform one single run in the test set for submission, so that no accidental overfitting occurs in the test set.

## References

**[1]**   MedlinePlus (Internet). Bethesda (MD): National Library of Medicine (US). Available from: [https://medlineplus.gov/](https://medlineplus.gov/).
