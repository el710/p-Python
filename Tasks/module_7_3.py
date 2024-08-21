from os import system

class WordsFinder():

    def __init__(self, *files_list) -> None:
        self.file_names = []
        for item in files_list:
            self.file_names.append(item)

    def get_all_words(self):
        punkt = [',', '.', '=', '!', '?', ';', ':', ' - ']
        all_words = {} ## {<filename>: [word1, word2], ...}

        for _filename in self.file_names:
            with open(_filename, encoding='utf-8') as file:
                all_words[_filename] = list()
                for line in file:
                    for i in punkt:
                        line = line.lower().replace(i, '')
                    for i in line.split():
                        all_words[_filename].append(i)

        return all_words

    def find(self, search_word, _how = 'first'):
        all_words = self.get_all_words()
        result_dict = {}
        for _filename, _dict in all_words.items():
            _is_find = 0
            for _id, _word in enumerate(_dict):
                if str.lower(search_word) == _word:
                    if _how == 'first':
                        _is_find = _id + 1
                        break
                    else:
                        _is_find += 1
            if _is_find:
                result_dict[_filename] = _is_find
        return result_dict

    def count(self, search_word):
        return self.find(search_word, 'all')


if __name__ == '__main__':

    system('cls')
    print('Work with files & strings...\n')

    finder2 = WordsFinder('text_file.txt')
    print(finder2.get_all_words())
    print(finder2.find('TEXT'))
    print(finder2.count('teXT'))


    finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
    print(finder1.get_all_words())
    print(finder1.find('the'))
    print(finder1.count('the'))