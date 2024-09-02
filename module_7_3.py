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
        places = {}
        for value, key in self.get_all_words().items():
            if word.lower() in key:
                places[value] = key.index(word.lower()) + 1
        return places
    def count(self, word):
        amount = {}
        k = 0
        for value, key in self.get_all_words().items():
            if word.lower() in key:
                k += 1
                amount[value] = key.count(word.lower())
        return amount
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
