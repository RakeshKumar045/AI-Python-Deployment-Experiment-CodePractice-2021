import numpy as np

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

word = sent.rstrip().lower().replace('\r\n', '').replace('\n', '').split(' ')
counts = np.zeros(len(word_index_dict))
# TODO: initialize counts to a zero vector
# TODO: iterate through file and update counts

for i in word:
	counts[word_index_dict[i]] += 1

probs = counts / np.sum(counts)

with open('unigram_probs.txt', 'w') as file:
	file.write(str(probs))

fw = open('unigram_eval.txt', 'w')
with open('toy_corpus.txt', encoding='utf-16') as toy:
	# toy = toy.read()
	for line in toy:

		sent_prob = 1
		sent_len = len(line.strip().split(" "))

		for word in line.strip().split(" "):
			sent_prob *= probs[word_index_dict[word.strip().lower()]]
		perplexity = 1 / (pow(sent_prob, 1.0 / sent_len))
		fw.write(str(perplexity) + '\n')
fw.close()

with open('unigram_generation.txt', 'w') as f:
	for i in range(10):
		f.write(GENERATE(word_index_dict, probs, "unigram", 10, '<s>') + '\n')
# TODO: normalize and writeout counts.

'''
Q: Estimate (just by eyeballing) the proportion of the word types that occurred only once in this corpus. Do you think the proportion of words that occur only once would be higher or lower if we used a larger corpus (e.g., all 57000 sentences in Brown)? Why or why not?


'''
