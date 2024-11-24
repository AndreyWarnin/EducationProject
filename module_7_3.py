class WordsFinder:
    REPLACEABLE_SYMBOLS = [',', '.', '=', '!', '?', ';', ':', ' - ']

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='UTF-8') as file:
                strings = file.read()
                for symbol in self.REPLACEABLE_SYMBOLS:
                    strings = strings.replace(symbol, ' ')
                words = strings.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        word_file_positions = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            positions = len(words)
            for position in range(positions):
                if word == words[position].lower():
                    word_file_positions[file_name] = position + 1
                    break
        return word_file_positions

    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        file_word_amount = {}
        for file_name, words in all_words.items():
            counter = 0
            for w in words:
                if word == w.lower():
                    counter += 1
            file_word_amount[file_name] = counter
        return file_word_amount


finder = WordsFinder('products.txt', 'test_1.txt')
dict_1 = finder.find('TEXT')
dict_2 = finder.count('teXT')
print(dict_1)
print(dict_2)