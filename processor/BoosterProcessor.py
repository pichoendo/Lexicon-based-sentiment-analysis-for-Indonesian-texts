from processor.WordProcessor import WordProcessor

class BoosterProcessor(WordProcessor):
    def __init__(self, boosterwords_dict):
        self.boosterwords_dict = boosterwords_dict

    def process(self, term):
        return self.boosterwords_dict.get(term, 0)
