#!/usr/bin/env python3

"""
ENLP A1: N-Gram Language Models

@author: Klinton Bicknell, Harry Eldridge, Nathan Schneider

DO NOT SHARE/DISTRIBUTE SOLUTIONS WITHOUT THE INSTRUCTOR'S PERMISSION
"""
import json as j

word_index_dict = {}


def read_file(filename):
	with open(filename + '.txt', encoding='utf-16') as f:
		data = f.read()
	f.close()
	return data


def save_file(filename, value):
	with open(filename + '.txt', 'w') as f:
		f.write(j.dumps(value))
	f.close()


# TODO: read brown_vocab_100.txt into word_index_dict
vocab = read_file("brown_vocab_100")
text = vocab.rstrip().replace('\n', ' ').split(' ')
for ind, value in enumerate(text):
	word_index_dict[value] = ind

# TODO: write word_index_dict to word_to_index_100.txt
save_file("word_to_index_100", word_index_dict)

print(word_index_dict['all'])
print(word_index_dict['resolution'])
print(len(word_index_dict))
