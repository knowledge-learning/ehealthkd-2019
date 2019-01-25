---
title: index
permalink: /
---

# IberLEF eHealth-KD 2019: eHealth Knowledge Discovery

## Description of the Task

Natural Language Processing (NLP) methods are increasingly being used to mine knowledge from unstructured health texts. Recent advances in health text processing techniques are encouraging researchers and health domain experts to go beyond just reading the information included in published texts (e.g. academic manuscripts, clinical reports, etc.) and structured questionnaires, to discover new knowledge by mining health contents. This has allowed other perspectives to surface that were not previously available.

Over the years many eHealth challenges have taken place, which have attempted to identify, classify, extract and link knowledge, such as Semevals, CLEF campaigns and others [1].

Inspired by previous NLP shared tasks like "[Semeval-2017 Task 10: ScienceIE](http://alt.qcri.org/semeval2017/task10/)" and research lines like Teleologies [2],both not specifically focussed on the health area, and related previous TASS challenges, eHealth-KD 2019 proposes -- as the previous edition eHealth-KD 2018--  modeling the human language in a scenario in which Spanish electronic health documents could be machine readable from a semantic point of view. With this task, we expect to encourage the development of software technologies to automatically extract a large variety of knowledge from eHealth documents written in the Spanish Language.

Even though this challenge is oriented to the health domain, the structure of the knowledge to be extracted is general-purpose. An example is provided in the following. The semantic structure proposed models four types of information units. Each one represents a specific semantic interpretation, and they make use of thirteen semantic relations among them. The following sections provide a detailed presentation of each unit and relation type.

The documents used as corpus have been taken from MedlinePlus and manually processed to make them fit for the task. Additional details are provided at the end of this document.

To simplify the evaluation process, two subtasks are presented:

1. Identification and classification phrases
2. Detection of semantic relations

## Subtask A: Identification and classification phrases

Given a list of eHealth documents written in Spanish, the goal of this subtask is to identify all the key phrases per document and their classes. These key phrases are all the relevant terms (single word or multiple words) that represent semantically important elements in a sentence. The following figure shows the relevant key phrases that appear in the example sentences shown in the previous section.

IMAGEN

Note that some key phrases (vías respiratorias and 60 años) span more than one word. Key phrases will always consist of one or more complete words (i.e., not a prefix or a suffix of a word), and will never include any surrounding punctuation symbols.
There are four categories or classes for key phrases:

* **Concept:** a general category that indicates the key phrase is a relevant term, concept, idea, in the knowledge domain of the sentence.
* **Action:** a concept that indicates a process or modification of other concepts. It can be indicated by a verb or verbal construction, such as afecta (affects), but also by nouns, such as exposición (exposition), where it denotes the act of being exposed to the Sun, and daños (damages), where it denotes the act of damaging the skin. It can also be used to indicate non-verbal functional relations, such as padre (parent), etc.
* **Predicate:** used to represent a function or filter of another set of elements, which has a semantic label in the text, such as mayores (older), and is applied to a concept, such as personas (people) with some additional arguments such as 60 años (60 years).
* **Reference:** A textual element that refers to a concept --of the same sentence or of different one--, which can be indicated by textual clues such as esta, aquel, etc.

Subtask A input is a text document with a sentence per line. All sentences have been tokenized at the word level (i.e., punctuation signs, parenthesis, etc, are separated from the surrounding text). The output consists of a plain text file, where each line represents a key phrase. Each line has the following format:
ID \tab START END ; START END \tab LABEL \tab TEXT
The ID is a numerical identifier that will be used in Subtask B to link key phrases with their  relations. The START and END indicate the starting and ending character of the text span. Multi-word phrases such as vías respiratorias where all the words are continuous can either be indicated by a single START / END pair or by several START / END (one for each word) separated by semicolons (;). Multi-word phrases where the words are not continuous must use semicolons to separate the different portions of the phrase. In the training documents we will always represent multi-word phrases separately for consistency.
The TEXT portion simply reproduces the full text of the key phrase. This portion will be ignored in the evaluation, so participants are free not to produce it, but it will be provided in all training documents, and we recommend participants to also produce it, since it simplifies manual inspection during development.
LABEL is one of the previous four categories defined. In this example, a possible output file is the following:

<script class="sample" src="https://gist-it.appspot.com/github/knowledge-learning/ehealthkd-v2/blob/master/docs/pages/sample_output_a.txt?footer=minimal"></script>

## Subtask B: Detection of semantic relations

Subtask B continues from the output of Subtask B, by linking the key phrases detected and labelled in each document. The purpose of this subtask is to recognize all relevant semantic relationships between the entities recognized. Eight of the thirteen semantic relations defined for this challenge can be identified in the following example:

IMAGEN








The semantic relations are divided in different categories:

**General relations (6):** general-purpose relations between two concepts (it involves Concept, Action, Predicate, and Reference) that have a specific semantic. When any of these relations applies, it is preferred over a domain relation --tagging a key phrase as a link between two information units--, since their 
semantic is independent of any textual label:

* **is-a:** indicates that one concept is a subtype, instance, or member of the class identified by the other.
* **same-as:** indicates that two concepts are semantically the same.
* *has-property:* indicates that one concept has a given property or characteristic.
* **part-of:** indicates that a concept is a constituent part of another.
* **causes:** indicates that one concept provoques the existence or occurrence of another.
* **entails:** indicates that the existence of one concept implies the existence or occurrence of another.

**Contextual relations (3):** allow to refine a concept (it involves Concept, Action, Predicate, and Reference) by attaching modifiers. These are:

* **in-time:** to indicate that something exists, occurs or is confined to a time-frame, such as in exposición in-time verano.
* **in-place:** to indicate that something exists, occurs or is confined to a place or location.
* **in-context:8* to indicate a general context in which something happens, like a mode, manner, or state, such as exposición in-context prolongada.

**Action roles (2):** indicate which role plays the concepts related to an Action:

* **subject:** indicates who performs the action, such as in [el] asma afecta [...].
* **target:** indicates who receives the effect of the action, such as in [...] afecta [las] vías respiratorias.
Actions can have several subjects and targets, in which case the semantic interpreted is that the union of the subjects performs the action over each of the targets.

**Predicate roles (2):** indicate which role plays the concepts related to a Predicate:

* **domain:** indicates the main concept on which the predicate applies.
* **arg:** indicates an additional concept that specifies a value for the predicate to make sense. The exact semantic of this argument depends on the semantic of the predicate label, such as in mayores [de] 60 años, where the predicate label mayores indicates that 60 años is a quantity, that restricts the minimum age for the predicate to be true.

The output for Subtask B is a plain text file where each line corresponds to a semantic relation between two key phrases, in the format:

```
LABEL \tab SOURCE-ID \tab DEST-ID
```

> **NOTE**: It doesn't really matter how many tabs exist between each column, but at least one tab must exist between columns.

The LABEL (i.e. column 1) is one of the previously defined, and the IDs correspond to the participants in the relation. Note that every relation is directed, hence the SOURCE-ID (i.e. column 2) and the DEST-ID (i.e column 3) must match the right direction, except for same-as which is symmetric, so both directions are equivalent. For the previous example the output is:

<script class="sample" src="https://gist-it.appspot.com/github/knowledge-learning/ehealthkd-v2/blob/master/docs/pages/sample_output_b.txt?footer=minimal"></script>

> **NOTE**: Column headers are optional, and only shown here for illustrative purposes.

### Evaluation measures and submission

This challenge proposes a main evaluation scenario (Scenario 1) where both subtasks previously described are performed in sequence. The submission that obtains the highest F1 score for the Scenario 1 will be considered the best overall performing system of the challenge. Additionally, participants will have the opportunity to address specific subtasks by submitting to two optional scenarios, once for each subtask. Scoring tables will be published also for each optional scenario.

## Main Evaluation (Scenario 1)

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
	Submissions and evaluation
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

## Discussion group
A Google Group will be set up for this “eHealth Shared Task” where announcements will be made. Do send your questions and feedback to (ehealth-kd@googlegroups.com).

## Chairs group
A Google Group will be set up for this “eHealth Shared Task” where announcements will be made. Do send your questions and feedback to (chairs_ehealth-kd@googlegroups.com).

## Funding
This research has been supported by a Carolina Foundation grant in agreement with University of Alicante and University of Havana, sponsoring to Suilan Estevez-Velarde. Moreover, it has also been partially funded by both aforementioned universities, Generalitat Valenciana, Spanish Government, Ministerio de Educación, Cultura y Deporte through the projects, TIN2015- 65100-R, TIN2015-65136-C2-2-R and PROMETEU/2018/089.
Contact
Yoan Gutiérrez Vázquez (ygutierrez@dlsi.ua.es)


## References

**[1]** Gonzalez-Hernandez, G. and Sarker, A. and O’Connor, K. and Savova, G. Capturing the Patient’s Perspective: a Review of Advances in Natural Language Processing of Health-Related Text. Yearbook of medical informatics; 26(01), p 214--227. 2017

**[2]**   Giunchiglia, F., & Fumagalli, M. (2017, November). Teleologies: Objects, Actions and Functions. In International Conference on Conceptual Modeling (pp. 520-534). Springer, Cham.

**[3]**   MedlinePlus [Internet]. Bethesda (MD): National Library of Medicine (US). Available from: https://medlineplus.gov/.
________________
[1] http://alt.qcri.org/semeval2017/task10/
[2] http://www.sepln.org/workshops/tass/2018/task-3/
