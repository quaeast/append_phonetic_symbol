import pandas as pd


def get_word_list():
    CSV_FILE_PATH = './words_dict.csv'
    word_list = pd.read_csv(CSV_FILE_PATH)
    return word_list


def get_phonetic(word_list, word):
    try:
        s = word_list.loc[word_list['word'] == word]['phonetic'].item()
        return s
    except Exception:
        return 'Not found!'


if __name__ == '__main__':
    my_word_list = get_word_list()
    get_phonetic(my_word_list, 'llllllll')
