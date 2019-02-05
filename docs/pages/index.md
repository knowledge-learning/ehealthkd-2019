---
title: Home
permalink: /
nav_order: 0
---

# IberLEF eHealth-KD 2019: eHealth Knowledge Discovery

Natural Language Processing (NLP) methods are increasingly being used to mine knowledge from unstructured health texts. Recent advances in health text processing techniques are encouraging researchers and health domain experts to go beyond just reading the information included in published texts (e.g. academic manuscripts, clinical reports, etc.) and structured questionnaires, to discover new knowledge by mining health contents. This has allowed other perspectives to surface that were not previously available.

Over the years many eHealth challenges have taken place, which have attempted to identify, classify, extract and link knowledge, such as Semevals, CLEF campaigns and others [1].

Inspired by previous NLP shared tasks like [Semeval-2017 Task 10: ScienceIE](http://alt.qcri.org/semeval2017/task10/) and research lines like Teleologies [2],both not specifically focussed on the health area, and related previous TASS challenges, eHealth-KD 2019 proposes --as the previous edition [eHealth-KD 2018](http://www.sepln.org/workshops/tass/2018/task-3/)--  modeling the human language in a scenario in which Spanish electronic health documents could be machine readable from a semantic point of view. With this task, we expect to encourage the development of software technologies to automatically extract a large variety of knowledge from eHealth documents written in the Spanish Language.

Even though this challenge is oriented to the health domain, the structure of the knowledge to be extracted is general-purpose. The semantic structure proposed models four types of information units. Each one represents a specific semantic interpretation, and they make use of thirteen semantic relations among them. The following sections provide a detailed presentation of each unit and relation type. An example is provided in the following picture.

![](img/task_b.png)

This challenge can be of interest for experts in the field of natural language processing, specifically for those working on automatic knowledge extraction and discovery. It is not a requirement to have expertise in health texts processing for dealing with the eHealth-KD task, due to the general purpose of the semantic schema defined. Nevertheless, eHealth researchers could find interesting this challenge to evaluate their technologies that rely on health domain knowledge.

## Description of the Subtasks

To simplify the evaluation process, two subtasks are presented:

1. [Identification and classification of phrases](tasks#subtask-a-identification-and-classification-of-phrases)
2. [Detection of semantic relations](tasks#subtask-b-detection-of-semantic-relations)

## Submissions and evaluation

The challenge will be graded in Codalab. [Details about submissions are provided here](evaluation).

There are three evaluation scenarios:
1. [A main scenario covering both tasks](evaluation#main-evaluation-scenario-1)
2. [An optional scenario evaluating subtask A](evaluation#optional-subtask-a-scenario-2)
3. [An optional scenario evaluation subtask B](evaluation#optional-subtask-b-scenario-3)

## Resources

All the data will be made available to participants in due time. This includes training, development and test data, as well as evaluation scripts and sample submissions. [More details are provided here](resources).

## Schedule

|Date|Event|
|---|---|
| **11 Feb 2018** | Trial data ready (**to be announced...**)| 
| **01 Apr 2019** | Training and development data ready (**to be announced...**)|
| **29 Apr 2019** | Registration deadline due by 23:59 GMT -12:00 |
| **30 Apr 2019** | Evaluation start* - Test data released (**to be announced...**)|
| **06 May 2019** | Evaluation end* - due by 23:59 GMT -12:00 |
| **13 May 2019** | Results posted (**to be announced...**)|
| **03 Jun 2019** | System description paper submissions due by 23:59 GMT -12:00 |
| **14 Jun 2019** | Paper reviews due |
| **17 Jun 2019** | Author notifications |
| **24 Jun 2019** | Camera ready submissions due |

## Organization committee

| Name                     | Email                                                 | Institution                   |
|--------------------------|-------------------------------------------------------|-------------------------------|
| Yoan Gutiérrez Vázquez   | [ygutierrez@dlsi.ua.es](mailto:ygutierrez@dlsi.ua.es) | University of Alicante, Spain |
| Suilan Estévez Velarde   | [sestevez@matcom.uh.cu](mailto:sestevez@matcom.uh.cu) | University of Havana, Cuba    |
| Alejandro Piad Morffis   | [apiad@matcom.uh.cu](mailto:apiad@matcom.uh.cu)       | University of Havana, Cuba    |
| Yudivián Almeida Cruz    | [yudy@matcom.uh.cu](mailto:yudy@matcom.uh.cu)         | University of Havana, Cuba    |
| Andrés Montoyo Guijarro  | [montoyo@dlsi.ua.es](mailto:montoyo@dlsi.ua.es)       | University of Alicante, Spain |
| Rafael Muñoz Guillena    | [rafael@dlsi.ua.es](mailto:rafael@dlsi.ua.es)         | University of Alicante, Spain |

### Discussion group

A Google Group will be set up for this “eHealth Shared Task” where announcements will be made.
Feel free to send your questions and feedback to [ehealth-kd@googlegroups.com](mailto:ehealth-kd@googlegroups.com).
General issues and feedback should be posted on our [Issues Page](https://github.com/knowledge-learning/ehealthkd-v2/issues) in Github.

### Previous version of the task

The eHealth-KD 2019 challenge is an enhanced version of the [TASS 2018 Task 3: eHealth Knowledge Discovery challenge](http://www.sepln.org/workshops/tass/2018/task-3/). In this new version, additional semantic types for key phrases and relations have been included, to cover a larger portion of the semantics of a sentence. These modifications increase the complexity of the task since a larger number of classes need to be predicted. However, we believe that these modifications provided higher semantic coverage.
Inspired by the successful participation of 6 teams in the previous version, and the insightful recommendations that many of the participants provided, we have redesigned this year’s task to be both more challenging and more objectively evaluated. Hence, we divided the evaluation scenarios so that each specific Subtask is evaluated independently, and also provide a scenario for evaluating the complete pipeline. We also merged previous year's Subtasks A and B since they are very similar in nature and complexity.

### Funding

This research has been supported by a Carolina Foundation grant in agreement with University of Alicante and University of Havana, sponsoring to Suilan Estévez Velarde. Moreover, it has also been partially funded by both aforementioned universities, Generalitat Valenciana, Spanish Government, Ministerio de Educación, Cultura y Deporte through the project PROMETEU/2018/089.

## References

**[1]** Gonzalez-Hernandez, G. and Sarker, A. and O’Connor, K. and Savova, G. Capturing the Patient’s Perspective: a Review of Advances in Natural Language Processing of Health-Related Text. Yearbook of medical informatics; 26(01), p 214--227. 2017

**[2]**   Giunchiglia, F., & Fumagalli, M. (2017, November). Teleologies: Objects, Actions and Functions. In International Conference on Conceptual Modeling (pp. 520-534). Springer, Cham.
