# module_7_3.py
# "Оператор "with"
import re


class WordsFinder:
    def __init__(self, *file_name):
        self.file_name = file_name
        self.file_names = []
        len_ = len(file_name)
        i = 0
        while i < len_:
            self.file_names.append(file_name[i])
            i += 1

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                file_read = file.read()
                file_read = re.sub('[!@#$%&*()+=;:?\n.,]', ' ', file_read)
                file_read = file_read.replace(' - ', ' ')
                file_read = file_read.replace('  ', ' ')
                file_read = file_read.replace('  ', ' ')
                file_read = file_read.strip()
                file_read = file_read.lower()
                file_read = file_read.split()
                all_words[file_name] = file_read
        return all_words

    def find_(self, word):
        word = word.lower()
        find_dict = {k: v.index(word) + 1 for k, v in self.get_all_words().items() if word in v}
        return find_dict

    def count(self, word):
        word = word.lower()
        count_dict = {k: v.count(word) for k, v in self.get_all_words().items() if word in v}
        return count_dict


finder1 = WordsFinder('test_file1.txt', 'test_file2.txt', 'test_file3.txt')

print(finder1.get_all_words())  # Все слова
print(finder1.find_('TEXT'))  # 3 слово по счёту
print(finder1.count('teXT'))  # 4 слова teXT в тексте всего
print(finder1.find_('123a'))
print(finder1.count('123a'))
