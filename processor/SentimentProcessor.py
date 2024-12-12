from processor.WordProcessor import WordProcessor


class SentimentProcessor(WordProcessor):
    def __init__(self, sentiwords_dict):
        self.sentiwords_dict = sentiwords_dict
    
    def process(self, term):
        return self.sentiwords_dict.get(term, 0)