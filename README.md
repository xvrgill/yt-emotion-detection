# YouTube Emotion Detection

## Dataset

The dataset used for this version of the project comes from the CASME database.

Data is subject to change depending on how applicable it will be for this use case.

## Encoding Feature Descriptions

### Subject

Numer (or id of sorts) given to a particular participant.

### Filename

The names of the video clips or directories containing the associated frames as images.

### OnsetF

The first frame for the micro-expression.

### Apex1

The first frame of the apex phase of the micro-expression.

### Apex2

The last frame of the apex phase of the micro-expression.

### OffsetF

The last frame of the micro expression.

### Onset

The duration from onset to apex 1 (the first frame of the apex phase of the micro-expression).

### Total

The duration from onset to offset.

### AU

Action units present in the video. Used to code a given emotion to each instance.

Emotion labeling is based **partly** on the AUs because micro-expressions are typically partial when given in low intensity. The self reports of the participants and the content of the video episodes were also used in labelling to account for htis.

Criteria for labelling using action units can be found in the `CASME.pdf` document in table 4.

### Emotion

The estimated emotion.

NOTE:

1. Amusement (in FG2013 paper) was replaced with happiness.
2. AU4 alone is difficult to judge which emotion it conveys.
It may indicate disgust, anger or attention/interest; we thus label "AU4" as "tense"
(for the moment). There are only very few micro-expression for some categories, so it
is also plausible to remove some categories for training and test, such as fear.