#!/usr/bin/env python3

"""
ENLP A1: N-Gram Language Models

@author: Klinton Bicknell, Harry Eldridge, Nathan Schneider

DO NOT SHARE/DISTRIBUTE SOLUTIONS WITHOUT THE INSTRUCTOR'S PERMISSION
"""

import numpy as np

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
word = brown.rstrip().lower().replace('\r\n', '').replace('\n', '').split(' ')

# TODO: initialize counts to a zero vector
array_size = len(word_index_dict)
counts = np.zeros(array_size)

# TODO: iterate through file and update counts

for ind in word:
	counts[word_index_dict[ind]] += 1

probs = counts / np.sum(counts)
print("probs : ", probs)

# save unigram_probs text file
save_file("unigram_probs", probs)

# write unigram_eval text file
file_write = open('unigram_eval.txt', 'w')

# read toy_corpus text file
with open('toy_corpus.txt', encoding='utf-8') as toy_corpus:
	for sent in toy_corpus:
		sent_prob = 1
		sent_len = len(sent.strip().split(" "))
		for word in sent.strip().split(" "):
			sent_prob *= probs[word_index_dict[word.strip().lower()]]
		perplexity = 1 / (pow(sent_prob, 1.0 / sent_len))
		file_write.write(str(perplexity) + '\n')
file_write.close()

# read unigram_generation text file
with open('unigram_generation.txt', 'w') as f:
	for i in range(10):
		f.write(GENERATE(word_index_dict, probs, "unigram", 10, '<s>') + '\n')

# TODO: normalize and writeout counts.
print("(the probability of ‘all’) is ", round(probs[0], 8))
print("(probability of ‘resolution’) is  ", round(probs[-1], 8))

f.close()
