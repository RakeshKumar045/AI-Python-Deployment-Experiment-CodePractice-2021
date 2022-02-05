#!/usr/bin/env python3

"""
ENLP A1: N-Gram Language Models

@author: Klinton Bicknell, Harry Eldridge, Nathan Schneider

DO NOT SHARE/DISTRIBUTE SOLUTIONS WITHOUT THE INSTRUCTOR'S PERMISSION
"""

import numpy as np


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


def bigram():
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

	my_dict = {}
	count = 0

	for word in bigram:
		for ind in range(len(bigram)):
			if bigram[ind] == word:
				count += 1
		my_dict[word] = count
		count = 0

	dict_list = []
	for ind, value in my_dict.items():
		temp = [ind, value]
		dict_list.append(temp)

	for i in range(len(dict_list)):
		x = word_index_dict[dict_list[i][0].split()[0]]
		y = word_index_dict[dict_list[i][0].split()[1]]
		counts[x, y] = dict_list[i][1]

	cnt_bi_unsth = counts.tolist()
	return cnt_bi_unsth, sent_split, word_index_dict


if __name__ == '__main__':
	# bigram
	cnt_bi_unsth, sent_split, word_index_dict = bigram()
	quest = ['in the past', 'in the time', 'the jury said', 'the jury recommended', 'jury said that',
			 'agriculture teacher ,']
	counts_tri = np.zeros(len(quest))

	tri_words = []
	for ind in range(len(sent_split) - 2):
		tri_words.append(sent_split[ind] + ' ' + sent_split[ind + 1] + ' ' + sent_split[ind + 2])

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
