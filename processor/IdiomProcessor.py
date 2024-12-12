from processor.WordProcessor import WordProcessor


class IdiomProcessor(WordProcessor):
    def __init__(self, idioms_dict):
        self.idioms_dict = idioms_dict

    def process(self, term):
        return self.idioms_dict.get(term, 0)