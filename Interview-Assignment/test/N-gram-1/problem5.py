import numpy as np


def bigram():
    with open('brown_vocab_100.txt', encoding='utf-16') as f:
        contents = f.read()

    final = contents.rstrip().replace('\n', ' ').split(' ')

    # create dict
    word_index_dict = {}
    for i, a in enumerate(final):
        word_index_dict[a] = i

    with open('brown_100.txt', encoding='utf-16') as f:
        sent = f.read()

    sent_split = sent.rstrip().lower().replace('\r\n', '').replace('\n', '').split(' ')

    s = (len(word_index_dict), len(word_index_dict))
    counts = np.zeros(s)  # TODO: initialize numpy 0s array

    # TODO: iterate through file and update counts
    # TODO: normalize counts
    # TODO: writeout bigram probabilities

    bi_words = []
    for i in range(len(sent_split) - 1):
        bi_words.append(sent_split[i] + ' ' + sent_split[i + 1])

    while '</s> <s>' in bi_words: bi_words.remove('</s> <s>')

    my_dict = {}
    c = 0

    for j in bi_words:
        for i in range(len(bi_words)):
            if bi_words[i] == j:
                c += 1
        my_dict[j] = c
        c = 0

    dict_list = []
    for key, value in my_dict.items():
        temp = [key, value]
        dict_list.append(temp)

    for i in range(len(dict_list)):
        x = word_index_dict[dict_list[i][0].split()[0]]
        y = word_index_dict[dict_list[i][0].split()[1]]
        counts[x, y] = dict_list[i][1]

    cnt_bi_unsth = counts.tolist()

    return cnt_bi_unsth, sent_split, word_index_dict


if __name__ == '__main__':

    # bigram unsmooth
    cnt_bi_unsth, sent_split, word_index_dict = bigram()

    # problem 5
    quest = ['in the past', 'in the time', 'the jury said', 'the jury recommended', 'jury said that',
             'agriculture teacher ,']
    counts_tri = np.zeros(len(quest))

    tri_words = []
    for i in range(len(sent_split) - 2):
        tri_words.append(sent_split[i] + ' ' + sent_split[i + 1] + ' ' + sent_split[i + 2])

    counts_tri = np.zeros(len(quest))
    for k in range(len(quest)):
        for i in tri_words:
            if quest[k] == i:
                counts_tri[quest.index(quest[k])] += 1

    for i in range(len(quest)):
        print('p({} | {}, {}):\tunsmoothed: {},\tsmoothed: {}'.format(quest[i].split()[2], quest[i].split()[0],
                                                                      quest[i].split()[1],
                                                                      counts_tri[i] / cnt_bi_unsth[
                                                                          word_index_dict[quest[i].split()[0]]][
                                                                          word_index_dict[quest[i].split()[1]]],
                                                                      (counts_tri[i] + 0.1) / (cnt_bi_unsth[
                                                                                                   word_index_dict[
                                                                                                       quest[i].split()[
                                                                                                           0]]][
                                                                                                   word_index_dict[
                                                                                                       quest[i].split()[
                                                                                                           1]]] + (
                                                                                                           0.1 * len(
                                                                                                       word_index_dict)))))
