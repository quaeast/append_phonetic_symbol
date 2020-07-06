import re
import phonetic

file_name = '/Users/fang/Desktop/词汇.md'

is_word = r'(\d+\.[\s\t\n]+)(\w+)(.*)'
has_phonetic = r'\d\.[\s\t\n]+\w+[\s\t\n]+\[.+\]'

word_list = phonetic.get_word_list()

file_lines_buffer = []

with open(file_name, 'r') as file:
    for line in file:
        isWordMatchObj = re.match(is_word, line, re.I)
        hasPhoneticMatchObj = re.match(has_phonetic, line, re.I)

        if isWordMatchObj and hasPhoneticMatchObj is None:
            striped_word = isWordMatchObj[2]
            word_phonetic = phonetic.get_phonetic(word_list, striped_word)
            line = isWordMatchObj[1] + isWordMatchObj[2] + ' [' + word_phonetic + ']' + isWordMatchObj[3] + '\n'

        file_lines_buffer.append(line)

with open(file_name[0:-3] + ' phonetic' + '.md', 'w+') as file:
    file.writelines(file_lines_buffer)
