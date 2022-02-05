#!/usr/bin/env python3

"""
ENLP A1: N-Gram Language Models

@author: Klinton Bicknell, Harry Eldridge, Nathan Schneider

DO NOT SHARE/DISTRIBUTE SOLUTIONS WITHOUT THE INSTRUCTOR'S PERMISSION
"""

import numpy as np
from sklearn.preprocessing import normalize

from generate import GENERATE


def read_file(filename):
    with open(filename + '.txt', encoding='utf-16') as f:
        data = f.read()
    f.close()
    return data


def save_file(filename, value):
    with open(filename + '.txt', 'w') as f:
        f.write(str(value))
    f.close()


def load_dict_from_file():
    f = open('word_to_index_100.txt', 'r')
    data = f.read()
    f.close()
    return eval(data)


vocab = read_file("brown_vocab_100")
text = vocab.rstrip().replace('\n', ' ').split(' ')

word_index_dict = load_dict_from_file()

brown = read_file("brown_100")
sent_split = brown.rstrip().lower().replace('\r\n', '').replace('\n', '').split(' ')

# TODO: initialize numpy 0s array
size = len(word_index_dict)
# TODO: normalize counts
counts = np.zeros((size, size))

# TODO: iterate through file and update counts
# TODO: writeout bigram probabilities
bigram = []
for i in range(len(sent_split) - 1):
    bigram.append(sent_split[i] + ' ' + sent_split[i + 1])

while '</s> <s>' in bigram:
    bigram.remove('</s> <s>')

dict = {}
count = 0
for word in bigram:
    for ind in range(len(bigram)):
        if bigram[ind] == word:
            count += 1
    dict[word] = count
    count = 0

dict_list = []
for ind, value in dict.items():
    temp = [ind, value]
    dict_list.append(temp)

for i in range(len(dict_list)):
    x = word_index_dict[dict_list[i][0].split()[0]]
    y = word_index_dict[dict_list[i][0].split()[1]]
    counts[x, y] = dict_list[i][1]

for i in range(len(counts)):
    for j in range(len(counts)):
        counts[i][j] += 0.1

probs = normalize(counts, norm='l1', axis=1)

print('p(the | all): {}'.format(round(probs[word_index_dict['all'], word_index_dict['the']], 7)))
print('p(jury | the): {}'.format(round(probs[word_index_dict['the'], word_index_dict['jury']], 7)))
print('p(campaign | the): {}'.format(round(probs[word_index_dict['the'], word_index_dict['campaign']], 7)))
print('p(calls | anonymous): {}'.format(round(probs[word_index_dict['anonymous'], word_index_dict['calls']], 7)))

with open('smooth_probs.txt', 'w') as file:
    file.write('p(the | all): {}\n'.format(probs[word_index_dict['all'], word_index_dict['the']]))
    file.write('p(jury | the): {}\n'.format(probs[word_index_dict['the'], word_index_dict['jury']]))
    file.write('p(campaign | the): {}\n'.format(probs[word_index_dict['the'], word_index_dict['campaign']]))
    file.write('p(calls | anonymous): {}\n'.format(probs[word_index_dict['anonymous'], word_index_dict['calls']]))

file_write = open('smooth_eval.txt', 'w')
with open('toy_corpus.txt', encoding='utf-8') as toy_corpus:
    for sent in toy_corpus:
        sent_prob = 1
        words = sent.strip().split(" ")
        sent_len = len(words)
        for word1, word2 in (words[i:i + 2] for i in range(0, len(words) - 1)):
            sent_prob *= probs[word_index_dict[word1.strip().lower()]][word_index_dict[word2.strip().lower()]]
        perplexity = 1 / (pow(sent_prob, 1.0 / sent_len))
        file_write.write(str(perplexity) + '\n')
file_write.close()

with open('smooth_generation.txt', 'w') as f:
    for i in range(10):
        f.write(GENERATE(word_index_dict, probs, "bigram", 10, '<s>') + '\n')
