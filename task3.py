from collections import Counter

class TextStats:
    def __init__(self, text):
        self.text = text

    def count_words(self):
        return len(self.text.split())

    def most_common_letter(self):
        letters = [c.lower() for c in self.text if c.isalpha()]
        counter = Counter(letters)
        return counter.most_common(1)[0] if counter else ('-', 0)
