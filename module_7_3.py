import io
import string
from pprint import pprint

class WordsFinder:
    def __init__(self, *files):
        self.file_names = list(files)
        self.all_words = {}
    def get_all_words(self):
        for file_name in self.file_names:
            with open(file_name, 'r') as file:
                text_file = file.read().lower().translate(str.maketrans('', '', string.punctuation)).split()
                self.all_words[file_name] = text_file
        return self.all_words
    def find(self, word):
        self.word = word.lower()
        k = 1
        for k, self.word in self.get_all_words().items():
            for i in self.all_words:
                if i == self.word:
                    k += 1
                if k != 0:
                    break
        return k, self.word
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))