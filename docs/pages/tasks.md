---
title: Tasks
permalink: /tasks
nav_order: 2
---

## Subtask A: Identification and classification of key phrases

Given a list of eHealth documents written in Spanish, the goal of this subtask is to identify all the key phrases per document and their classes. These key phrases are all the relevant terms (single word or multiple words) that represent semantically important elements in a sentence. The following figure shows the relevant key phrases that appear in the example sentences shown in the previous section.

![](img/task_a.png)

Note that some key phrases ("*vías respiratorias*" and "*60 años*") span more than one word. Key phrases will always consist of one or more complete words (i.e., not a prefix or a suffix of a word), and will never include any surrounding punctuation symbols.
There are four categories or classes for key phrases:

* **Concept:** a general category that indicates the key phrase is a relevant term, concept, idea, in the knowledge domain of the sentence.
* **Action:** a concept that indicates a process or modification of other concepts. It can be indicated by a verb or verbal construction, such as "*afect*a* (*affects*), but also by nouns, such as "*exposición*" (*exposition*), where it denotes the act of being exposed to the Sun, and "*daños*" (*damages*), where it denotes the act of damaging the skin. It can also be used to indicate non-verbal functional relations, such as "*padre*" (*parent*), etc.
* **Predicate:** used to represent a function or filter of another set of elements, which has a semantic label in the text, such as "*mayores*" (*older*), and is applied to a concept, such as "*personas*" (*people*) with some additional arguments such as "*60 años*" (*60 years*).
* **Reference:** A textual element that refers to a concept --of the same sentence or of different one--, which can be indicated by textual clues such as "*esta*", "*aquel*", etc.

Subtask A input is a text document with a sentence per line. All sentences have been tokenized at the word level (i.e., punctuation signs, parenthesis, etc, are separated from the surrounding text). The output consists of a plain text file, where each line represents a key phrase. Each line has the following format:

```
ID \tab START END ; START END \tab LABEL \tab TEXT
```

The **ID** is a numerical identifier that will be used in Subtask B to link key phrases with their relations. The **START** and **END** indicate the starting and ending character of the text span. Multi-word phrases such as vías respiratorias where all the words are continuous can either be indicated by a single **START / END** pair or by several **START / END** (one for each word) separated by semicolons (;). Multi-word phrases where the words are not continuous must use semicolons to separate the different portions of the phrase. In the training documents we will always represent multi-word phrases separately for consistency.
The **TEXT** portion simply reproduces the full text of the key phrase. This portion will be ignored in the evaluation, so participants are free not to produce it, but it will be provided in all training documents, and we recommend participants to also produce it, since it simplifies manual inspection during development.
**LABEL** is one of the previous four categories defined. In this example, a possible output file is the following:

<script class="sample" src="https://gist-it.appspot.com/github/knowledge-learning/ehealthkd-v2/blob/master/docs/sample_output_a.txt?footer=minimal"></script>

> **NOTE**: Column headers are optional, and only shown here for illustrative purposes.

> **Recap:** Columns are separated by _one or more_ **TAB** characters. The two numbers inside each **START/END** pair are separated by _one_ **SPACE** character. The different **START/END** pairs for each multi-word are separated by _one_ **SEMICOLON** ( **;** ) character.

## Subtask B: Detection of semantic relations

Subtask B continues from the output of Subtask B, by linking the key phrases detected and labelled in each document. The purpose of this subtask is to recognize all relevant semantic relationships between the entities recognized. Eight of the thirteen semantic relations defined for this challenge can be identified in the following example:

![](img/task_b.png)

The semantic relations are divided in different categories:

**General relations (6):** general-purpose relations between two concepts (it involves Concept, Action, Predicate, and Reference) that have a specific semantic. When any of these relations applies, it is preferred over a domain relation --tagging a key phrase as a link between two information units--, since their
semantic is independent of any textual label:

* **is-a:** indicates that one concept is a subtype, instance, or member of the class identified by the other.
* **same-as:** indicates that two concepts are semantically the same.
* **has-property:** indicates that one concept has a given property or characteristic.
* **part-of:** indicates that a concept is a constituent part of another.
* **causes:** indicates that one concept provoques the existence or occurrence of another.
* **entails:** indicates that the existence of one concept implies the existence or occurrence of another.

**Contextual relations (3):** allow to refine a concept (it involves **Concept**, **Action**, **Predicate**, and **Reference**) by attaching modifiers. These are:

* **in-time:** to indicate that something exists, occurs or is confined to a time-frame, such as in "*exposición*" in-time "*verano*".
* **in-place:** to indicate that something exists, occurs or is confined to a place or location.
* **in-context:** to indicate a general context in which something happens, like a mode, manner, or state, such as "*exposición*" in-context "*prolongada*".

**Action roles (2):** indicate which role plays the concepts related to an **Action**:

* **subject:** indicates who performs the action, such as in "*[el] asma afecta [...]*".
* **target:** indicates who receives the effect of the action, such as in "*[...] afecta [las] vías respiratorias*".
Actions can have several subjects and targets, in which case the semantic interpreted is that the union of the subjects performs the action over each of the targets.

**Predicate roles (2):** indicate which role plays the concepts related to a **Predicate**:

* **domain:** indicates the main concept on which the predicate applies.
* **arg:** indicates an additional concept that specifies a value for the predicate to make sense. The exact semantic of this argument depends on the semantic of the predicate label, such as in "*mayores [de] 60 años*", where the predicate label "*mayores*" indicates that "*60 años*" is a quantity, that restricts the minimum age for the predicate to be true.

The output for Subtask B is a plain text file where each line corresponds to a semantic relation between two key phrases, in the format:

```
LABEL \tab SOURCE-ID \tab DEST-ID
```

The **LABEL** (i.e. column 1) is one of the previously defined, and the **ID**s correspond to the participants in the relation. Note that every relation is directed, hence the **SOURCE-ID** (i.e. column 2) and the **DEST-ID** (i.e column 3) must match the right direction, except for **same-as** which is symmetric, so both directions are equivalent. For the previous example the output is:

<script class="sample" src="https://gist-it.appspot.com/github/knowledge-learning/ehealthkd-v2/blob/master/docs/sample_output_b.txt?footer=minimal"></script>

> **NOTE**: Column headers are optional, and only shown here for illustrative purposes.

> **Recap:** Columns are separated by _one or more_ **TAB** characters.
