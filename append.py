import re
import phonetic

line = '1. a'
is_word = r'\d+\.*'
has_phonetic = r'\d\.[\s\t\n]+\w+[\s\t\n]+\[.+\]'

file_name = '/Users/fang/Desktop/词汇.md'

word_list = phonetic.get_word_list()

file_lines_buffer = []

file = open(file_name, 'r')
for line in file:
    isWordMatchObj = re.match(is_word, line, re.M | re.I)
    hasPhoneticMatchObj = re.match(has_phonetic, line, re.M | re.I)

    # print(hasPhoneticMatchObj)
    if isWordMatchObj and hasPhoneticMatchObj is None:
        word = re.match(r'\d+.[\s\t\n]+\w+', line, re.M | re.I).group()
        striped_word = re.sub(r'\d+.[\s\t\n]+', '', word)
        word_phonetic = phonetic.get_phonetic(word_list, striped_word)
        line = line.rstrip() + ' [' + word_phonetic + ']' + '\n'

    file_lines_buffer.append(line)

file = open(file_name[0:-3] + ' new' + '.md', 'w+')
for line in file_lines_buffer:
    file.writelines(line)
