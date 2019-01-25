---
title: Resources
permalink: /resources
---

# Linguistic resources

As in the previous edition, the corpus for eHealth-KD 2019 will be extracted from MedlinePlus sources.
This platform freely provides large health textual data from which we have made a selection for constituting the eHealth-KD corpus. The selection has been made by sampling specific XML files from the collection available in the [Medline website](https://medlineplus.gov/xml.html).

> "MedlinePlus is the National Institutes of Health's Website for patients and their families and friends. Produced by the National Library of Medicine, the world’s largest medical library, it brings you information about diseases, conditions, and wellness issues in language you can understand. MedlinePlus offers reliable, up-to-date health information, anytime, anywhere, for free." [3]

These files contain several entries related to health and medicine topics and have been processed to remove all XML markup to extract the textual content. Only Spanish language items were considered. Once cleaned, each individual item was converted to a plain text document, and some further post-processing is applied to remove unwanted sentences, such as headers, footers and similar elements, and to flatten HTML lists into plain sentences. The final documents are manually tagged using Brat by a group of annotators. After tagging, a post-processing was applied to Brat’s output files (ANN format) to obtain the output files in the formats described in this document.

The resulting documents and output files are distributed along with the Task. There is no need for participants to download extra data from MedlinePlus servers, since all the input is already distributed.

# Additional resources

Participants may freely use any additional resources they consider necessary to improve their systems, from other corpora (annotated or not), to external knowledge either explicitly (i.e., using knowledge bases) or implicitly (i.e., captured in word embeddings). For the purpose of sharing the results we expect participants to fully disclose everything they use.
However, participants may not manually annotate the test set, since doing so would be in violation of the ethics of the competition. Furthermore, we expect participants to perform all the fine tuning using only the training and development, and then perform one single run in the test set for submission, so that no accidental overfitting occurs in the test set.
