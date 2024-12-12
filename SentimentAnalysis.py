import json
import numpy as np
import pandas as pd

from processor.SentimentProcessor import SentimentProcessor
from processor.EmoticonProcessor import EmoticonProcessor
from processor.IdiomProcessor import IdiomProcessor
from processor.BoosterProcessor import BoosterProcessor
class SentimentAnalysis:
    def __init__(self, config=dict()):
        with open('data/dict.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        self.negasi = set(data['negasi'])  # Assuming 'negasi' is an array of strings in the JSON

        # Process the word dictionaries from the JSON
        # Convert data for each category into a dictionary (term: score)
        self.sentiwords_dict = {item['item']: item['value'] for item in data['kata']}
        self.emoticon_dict = {item['item']: item['value'] for item in data['emoticon']}
        self.idioms_dict = {item['item']: item['value'] for item in data['idiom']}
        self.boosterwords_dict = {item['item']: item['value'] for item in data['booster']}

        # Optionally, convert the dictionaries to pandas DataFrames for easier handling if needed
        self.sentiwords_df = pd.DataFrame(list(self.sentiwords_dict.items()), columns=["term", "score"])
        self.emoticon_df = pd.DataFrame(list(self.emoticon_dict.items()), columns=["term", "score"])
        self.idioms_df = pd.DataFrame(list(self.idioms_dict.items()), columns=["term", "score"])
        self.boosterwords_df = pd.DataFrame(list(self.boosterwords_dict.items()), columns=["term", "score"])

        # Configure processors
      
        self.sentiment_processor = SentimentProcessor(self.sentiwords_dict)
        self.emoticon_processor = EmoticonProcessor(self.emoticon_dict)
        self.idiom_processor = IdiomProcessor(self.idioms_dict)
        self.booster_processor = BoosterProcessor(self.boosterwords_dict)

        # Configuration settings
        self.negation_conf = config.get("negation", True)
        self.booster_conf = config.get("booster", True)
        self.ungkapan_conf = config.get("ungkapan", True)

    def process_sentence(self, sentence):
        terms = sentence.split()
    
        scores = np.zeros(len(terms))

        for i, term in enumerate(terms):
            score = self.sentiment_processor.process(term)  # Sentiment score

            # Handle negation
            if self.negation_conf and i > 0 and terms[i-1] in self.negasi:
                score = -score if score != 0 else score

            # Handle booster words
            if self.booster_conf and i > 0 and self.booster_processor.process(terms[i-1]) != 0:
                score += self.booster_processor.process(terms[i-1])

            # Handle emoticons
            if self.emoticon_processor.process(term) != 0:
                score += self.emoticon_processor.process(term)

            # Handle idioms
            if self.ungkapan_conf and self.idiom_processor.process(' '.join(terms[i:i+2])) != 0:
                score = self.idiom_processor.process(' '.join(terms[i:i+2]))

            scores[i] = score

        return scores

    def classify(self, scores):
        max_score = np.max(scores)
        min_score = np.min(scores)
        return 1 if max_score > abs(min_score) else 0

    def analysis(self, sentence):
        sentences = sentence.split('.')
        all_scores = np.array([])

        for sent in sentences:
            scores = self.process_sentence(sent)
            all_scores = np.append(all_scores, scores)

        result = self.classify(all_scores)
        return {
            "classified_text": sentence,
            "scores": all_scores.tolist(),
            "classification": "POSITIVE" if result == 1 else "NEGATIVE"
        }
