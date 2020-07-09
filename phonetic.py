import pandas as pd


def get_word_list():
    CSV_FILE_PATH = './words_dict.csv'
    word_list = pd.read_csv(CSV_FILE_PATH)
    return word_list


def get_phonetic(word_list, word):
    try:
        s = word_list.loc[word_list['word'] == word]['phonetic'].item()
        if isinstance(s, str):
            return '[' + s + ']'
        else:
            return ''
    except Exception:
        return ''


if __name__ == '__main__':
    my_word_list = get_word_list()
    print(get_phonetic(my_word_list, 'ganster'))
