# Sentiment Analysis with Custom Lexicon

This project implements a sentiment analysis system that uses a custom lexicon-based approach. It processes sentences to evaluate their sentiment by leveraging various word categories like sentiment words, emoticons, idioms, and booster words.

## Features

- Sentiment analysis based on custom lexicons (sentiment words, emoticons, idioms, booster words).
- Handle negations, booster words, emoticons, and idioms.
- Remove stopwords to improve accuracy.
- Efficient processing using `pandas` and `numpy`.

## Prerequisites

- Python 3.7 or higher
- Required Python libraries:
  - `pandas`
  - `numpy`
  - `scikit-learn`
  - `re`

You can install the dependencies using the following command:

```bash
pip install pandas numpy scikit-learn
```

## How It Works
1. Sentiment Analysis
The sentiment analysis system processes the input sentence by breaking it down into words (or terms) and then assigns sentiment scores to each term using a custom lexicon.

2. Lexicons
Custom lexicons are used to define the sentiment of words:

Sentiwords: General sentiment words (positive/negative).
Emoticons: Emoticons with sentiment association (e.g., ":)" = positive).
Idioms: Common phrases that have a specific sentiment.
Booster Words: Words that amplify the sentiment (e.g., "really", "very").

3. Stopword Removal
Stopwords (common words like "the", "is", etc.) are removed to improve the accuracy of sentiment scoring.

4. Negation Handling
If a negation word (like "not") precedes a sentiment word, the sentiment score of that word is reversed.

5. Booster and Idioms
Booster words are used to amplify the sentiment score, and idioms have predefined sentiment values that override the individual word values.

6. Classification
After calculating sentiment scores for all words in the sentence, the overall sentiment is classified as either Positive or Negative based on the maximum sentiment score.
