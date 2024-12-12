from processor.WordProcessor import WordProcessor
class EmoticonProcessor(WordProcessor):
    def __init__(self, emoticon_dict):
        self.emoticon_dict = emoticon_dict

    def process(self, term):
        return self.emoticon_dict.get(term, 0)
