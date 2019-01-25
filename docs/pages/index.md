---
title: Home
permalink: /
---

# IberLEF eHealth-KD 2019: eHealth Knowledge Discovery

Natural Language Processing (NLP) methods are increasingly being used to mine knowledge from unstructured health texts. Recent advances in health text processing techniques are encouraging researchers and health domain experts to go beyond just reading the information included in published texts (e.g. academic manuscripts, clinical reports, etc.) and structured questionnaires, to discover new knowledge by mining health contents. This has allowed other perspectives to surface that were not previously available.

Over the years many eHealth challenges have taken place, which have attempted to identify, classify, extract and link knowledge, such as Semevals, CLEF campaigns and others [1].

Inspired by previous NLP shared tasks like [Semeval-2017 Task 10: ScienceIE](http://alt.qcri.org/semeval2017/task10/) and research lines like Teleologies [2],both not specifically focussed on the health area, and related previous TASS challenges, eHealth-KD 2019 proposes --as the previous edition [eHealth-KD 2018](http://www.sepln.org/workshops/tass/2018/task-3/)--  modeling the human language in a scenario in which Spanish electronic health documents could be machine readable from a semantic point of view. With this task, we expect to encourage the development of software technologies to automatically extract a large variety of knowledge from eHealth documents written in the Spanish Language.

Even though this challenge is oriented to the health domain, the structure of the knowledge to be extracted is general-purpose. An example is provided in the following. The semantic structure proposed models four types of information units. Each one represents a specific semantic interpretation, and they make use of thirteen semantic relations among them. The following sections provide a detailed presentation of each unit and relation type.

The documents used as corpus have been taken from MedlinePlus and manually processed to make them fit for the task. Additional details are provided at the end of this document.

## Description of the Subtasks

To simplify the evaluation process, two subtasks are presented:

1. [Identification and classification of phrases](tasks/#identification-and-classification-of-phrases)
2. [Detection of semantic relations](tasks/#detection-of-semantic-relations)

## Evaluation measures and submission

This challenge proposes a main evaluation scenario (Scenario 1) where both subtasks previously described are performed in sequence. The submission that obtains the highest F1 score for the Scenario 1 will be considered the best overall performing system of the challenge. Additionally, participants will have the opportunity to address specific subtasks by submitting to two optional scenarios, once for each subtask. Scoring tables will be published also for each optional scenario.

### Main Evaluation (Scenario 1)

This scenario evaluates all of the subtasks together as a pipeline. The input consists only of a plain text, and the expected output will be the two output files for Subtask A and B, as described before. The measures will be precision, recall and F1 as follows:


The exact definition of Correct, Missing, Spurious, Partial and Incorrect is presented in the following sections for each subtask. Then, a standard F1 is computed.

F1 will determine the ranking of Scenario 1 and consequently of the eHealthKD challenge.

### Optional Subtask A (Scenario 2)

This scenario only evaluates Subtask A. The input is a plain text with several sentences and the output is as described in Subtask A. To compute the scores we define correct, partial, missing, incorrect and spurious matches. The expected and actual output files do not need to agree on the ID for each phrase, nor on their order. The evaluator matches are based on the START and END values and LABEL. A brief description about the metrics follows:


* **Correct matches** are reported when a text in the dev file matches exactly with a corresponding text span in the gold file in START and END values, and also LABEL. Only one correct match per entry in the gold file can be matched. Hence, duplicated entries will count as Spurious.
* **Incorrect matches** are reported when START and END values match, but not the LABEL.
* **Partial matches** are reported when two intervals [START, END] have a non-empty intersection, such as the case of “vías respiratorias” and “respiratorias” in the previous example (and matching LABEL). Notice that a partial phrase will only be matched against a single correct phrase. For example, “tipo de cáncer” could be a partial match for both “tipo” and “cáncer”, but it is only counted once as a partial match with the word “tipo”. The word “cancer” is counted then as Missing. This aims to discourage a few large text spans that cover most of the document from getting a very high score.
* **Missing matches** are those that appear in the gold file but not in the dev file.
* **Spurious matches** are those that appear in the dev file but not in the gold file.


From these definitions, we compute precision, recall, and a standard F1 measure as follows:





	A higher precision means that the number of spurious identifications is smaller compared to the number of missing identifications, and a higher recall means the opposite. Partial matches are given half the score of correct matches, while missing and spurious identifications are given no score.


F1 will determine the ranking of Scenario 2.

### Optional Subtask B (Scenario 3)

This scenario only evaluates Subtask B. The input is plain text and the correct outputs from Subtask A. The expected output is as described in Subtask C. Similarly to previous scenarios, we define the correct, missing and spurious items, defined as follows:

* **Correct:** relationships that matched exactly to the gold file, including the LABEL and the corresponding IDs for each of the participants.
* **Missing:** relationships that are in the gold file but not in the dev file, either because the LABEL is wrong, or because one of the IDs didn’t match.
* **Spurious:** relationships that are in the dev file but not in the gold file, either because the LABEL is wrong, or because one of the IDs didn’t match.


We define standard precision, recall and F1 metrics as follows:





	F1 will determine the ranking of Scenario 3.


NOTE: The Scenario 1 is more complex than solving each optional scenario separately, since errors in subtask A will necessary translate to errors in subtask B. For this reason it is considered the main evaluation metric. Additionally, this scenario also provides the possibility for integrated end-to-end solutions that solve both subtask simultaneously.

## Submissions and evaluation
The challenge will be graded on Codalab (exact details will be provided in the official announcement). However, a fully working evaluation script will be provided to participants, that exactly matches the evaluation formulas used in Codalab. This way participants will have the possibility to evaluate their systems offline and perform hyper-parameter tuning with respect to the same evaluation metrics as used in the competition.
The corpus will be divided into three sections. Training and development sets will be published along with baseline implementations, for participants to train and fine-tune their systems. These files will consist of both plain text input and the expected outputs for both subtasks. Afterward, a small test set will be released, with plain text only, further divided into 3 sub-sets, one for each scenario. Participants are expected to submit the corresponding output files to Codalab.


In no case, participants will be able to access the correct output files for the test set before the challenge ends. Afterward, the full corpus, including Brat-annotated files will be freely available under a suitable license for the research community.

## Target community

This challenge can be of interest for experts in the field of natural language processing, specifically for those working on automatic knowledge extraction and discovery. It is not a requirement to have expertise in health texts processing for dealing with the eHealth-KD task, due to the general purpose of the semantic schema defined. Nevertheless, eHealth researchers could find interesting this challenge to evaluate their technologies that rely on health domain knowledge.

## Previous version of the task
The eHealth-KD 2019 challenge is an enhanced version of the TASS 2018 Task 3: eHealth Knowledge Discovery challenge. In this new version, additional semantic types for key phrases and relations have been included, to cover a larger portion of the semantics of a sentence. These modifications increase the complexity of the task since a larger number of classes need to be predicted. However, we believe that these modifications provided higher semantic coverage.
Inspired by the successful participation of 6 teams in the previous version, and the insightful recommendations that many of the participants provided, we have redesigned this year’s task to be both more challenging and more objectively evaluated. Hence, we divided the evaluation scenarios so that each specific Subtask is evaluated independently, and also provide a scenario for evaluating the complete pipeline.

## Linguistic resources
As in the previous edition, the corpus for eHealth-KD 2019 will be extracted from MedlinePlus sources. “MedlinePlus is the National Institutes of Health's Website for patients and their families and friends. Produced by the National Library of Medicine, the world’s largest medical library, it brings you information about diseases, conditions, and wellness issues in language you can understand. MedlinePlus offers reliable, up-to-date health information, anytime, anywhere, for free.” [3] This platform freely provides large health textual data from which we have made a selection for constituting the eHealth-KD corpus. The selection has been made by sampling specific XML files from the collection available in https://medlineplus.gov/xml.html.

These files contain several entries related to health and medicine topics and have been processed to remove all XML markup to extract the textual content. Only Spanish language items were considered. Once cleaned, each individual item was converted to a plain text document, and some further post-processing is applied to remove unwanted sentences, such as headers, footers and similar elements, and to flatten HTML lists into plain sentences. The final documents are manually tagged using Brat by a group of annotators. After tagging, a post-processing was applied to Brat’s output files (ANN format) to obtain the output files in the formats described in this document.


The resulting documents and output files are distributed along with the Task. There is no need for participants to download extra data from MedlinePlus servers, since all the input is already distributed.
Additional resources:
Participants may freely use any additional resources they consider necessary to improve their systems, from other corpora (annotated or not), to external knowledge either explicitly (i.e., using knowledge bases) or implicitly (i.e., captured in word embeddings). For the purpose of sharing the results we expect participants to fully disclose everything they use.
However, participants may not manually annotate the test set, since doing so would be in violation of the ethics of the competition. Furthermore, we expect participants to perform all the fine tuning using only the training and development, and then perform one single run in the test set for submission, so that no accidental overfitting occurs in the test set.

## Schedule

|Date|Event|
|---|---|
| **11 Feb 2018** | Trial data ready |
| **01 Apr 2019** | Training and development data ready |
| **29 Apr 2019** | Registration deadline due by 23:59 GMT -12:00 |
| **30 Apr 2019** | Evaluation start* - Test data released |
| **06 May 2019** | Evaluation end* - due by 23:59 GMT -12:00 |
| **13 May 2019** | Results posted |
| **03 Jun 2019** | System description paper submissions due by 23:59 GMT -12:00 |
| **14 Jun 2019** | Paper reviews due |
| **17 Jun 2019** | Author notifications |
| **24 Jun 2019** | Camera ready submissions due |

## Organization committee

| Name |	Email |	Institution |
|-|-|-|
| Yoan Gutiérrez Vázquez | ygutierrez@dlsi.ua.es | University of Alicante, Spain |
| Suilan Estévez Velarde | sestevez@matcom.uh.cu | University of Havana, Cuba |
| Yudivián Almeida Cruz | yudy@matcom.uh.cu | University of Havana, Cuba |
| Alejandro Piad Morffis | apiad@matcom.uh.cu | University of Havana, Cuba |
| Andrés Montoyo Guijarro | montoyo@dlsi.ua.es | University of Alicante, Spain |
| Rafael Muñoz Guillena | rafael@dlsi.ua.es | University of Alicante, Spain |

### Discussion group

A Google Group will be set up for this “eHealth Shared Task” where announcements will be made. Do send your questions and feedback to (ehealth-kd@googlegroups.com).

### Chairs group

A Google Group will be set up for this “eHealth Shared Task” where announcements will be made. Do send your questions and feedback to (chairs_ehealth-kd@googlegroups.com).

### Funding

This research has been supported by a Carolina Foundation grant in agreement with University of Alicante and University of Havana, sponsoring to Suilan Estevez-Velarde. Moreover, it has also been partially funded by both aforementioned universities, Generalitat Valenciana, Spanish Government, Ministerio de Educación, Cultura y Deporte through the projects, TIN2015- 65100-R, TIN2015-65136-C2-2-R and PROMETEU/2018/089.

### Contact

Yoan Gutiérrez Vázquez ([ygutierrez@dlsi.ua.es]())


## References

**[1]** Gonzalez-Hernandez, G. and Sarker, A. and O’Connor, K. and Savova, G. Capturing the Patient’s Perspective: a Review of Advances in Natural Language Processing of Health-Related Text. Yearbook of medical informatics; 26(01), p 214--227. 2017

**[2]**   Giunchiglia, F., & Fumagalli, M. (2017, November). Teleologies: Objects, Actions and Functions. In International Conference on Conceptual Modeling (pp. 520-534). Springer, Cham.

**[3]**   MedlinePlus (Internet). Bethesda (MD): National Library of Medicine (US). Available from: [https://medlineplus.gov/]().
