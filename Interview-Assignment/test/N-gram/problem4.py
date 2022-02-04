import numpy as np
from sklearn.preprocessing import normalize

from generate import GENERATE

# dict
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
# bi_words.remove('</s> <s>')
# print(bi_words[0:29])

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

# print(str(x)+" "+str(y))
for i in range(len(counts)):
	for j in range(len(counts)):
		counts[i][j] += 0.1

probs = normalize(counts, norm='l1', axis=1)

# print('p(jury | the): ',probs[604,80])
with open('smooth_probs.txt', 'w') as file:
	file.write('p(the | all): {}\n'.format(probs[word_index_dict['all'], word_index_dict['the']]))
	file.write('p(jury | the): {}\n'.format(probs[word_index_dict['the'], word_index_dict['jury']]))
	file.write('p(campaign | the): {}\n'.format(probs[word_index_dict['the'], word_index_dict['campaign']]))
	file.write('p(calls | anonymous): {}\n'.format(probs[word_index_dict['anonymous'], word_index_dict['calls']]))

# np.savetxt('smooth_probs.txt', probs, fmt="%f")
fw = open('smooth_eval.txt', 'w')
with open('toy_corpus.txt', encoding='utf-16') as toy:
	# toy = toy.read()
	for line in toy:

		sent_prob = 1
		words = line.strip().split(" ")
		sent_len = len(words)

		for word1, word2 in (words[i:i + 2] for i in range(0, len(words) - 1)):
			sent_prob *= probs[word_index_dict[word1.strip().lower()]][word_index_dict[word2.strip().lower()]]
		perplexity = 1 / (pow(sent_prob, 1.0 / sent_len))
		fw.write(str(perplexity) + '\n')
fw.close()

with open('smooth_generation.txt', 'w') as f:
	for i in range(10):
		f.write(GENERATE(word_index_dict, probs, "bigram", 10, '<s>') + '\n')
'''
Q: Why did all four probabilities go down in the smoothed model? Now note that the probabilities did not all decrease by the same amount. In particular, the two probabilities conditioned on ‘the’ dropped only slightly, while the other two probabilities (conditioned on ‘all’ and ‘anonymous’) dropped rather dramatically. Q: Why did add-α smoothing cause probabilities conditioned on ‘the’ to fall much less than these others? And why is this behavior (causing probabilities conditioned on ‘the’ to fall less than the others) a good thing? In figuring this out, you may find it useful to look at the relevant individual rows of the counts matrix (prior to adding the 0.1) to see how they’re different. In numpy, you can look at nth row of the counts matrix using counts[n,].
'''
