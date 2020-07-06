import re
import phonetic

file_name = '/Users/fang/Desktop/词汇.md'

is_word = r'(\d+\.[\s\t\n]+)(\w+)(.*)'
has_phonetic = r'\d\.[\s\t\n]+\w+[\s\t\n]+\[.+\]'

word_list = phonetic.get_word_list()

file_lines_buffer = []

with open(file_name, 'r') as file:
    for line in file:
        is_word_match_obj = re.match(is_word, line, re.I)
        has_phonetic_match_obj = re.match(has_phonetic, line, re.I)

        if is_word_match_obj and has_phonetic_match_obj is None:
            striped_word = is_word_match_obj[2]
            word_phonetic = phonetic.get_phonetic(word_list, striped_word)
            line = is_word_match_obj[1] + is_word_match_obj[2] + ' [' + word_phonetic + ']' + is_word_match_obj[3] + '\n'

        file_lines_buffer.append(line)

with open(file_name[0:-3] + ' phonetic' + '.md', 'w+') as file:
    file.writelines(file_lines_buffer)
