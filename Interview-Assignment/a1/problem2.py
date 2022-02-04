import re

import numpy as np


def load_dict_from_file():
    f = open('word_to_index_100.txt', 'r')
    data = f.read()
    f.close()
    return eval(data)


word_index_dict = load_dict_from_file()

with open("brown_100.txt") as f:
    brown = [line.rstrip('\n') for line in f]

f.close()


def count_word(word_input, word_index_dict_input):
    count_vector = np.zeros(813, dtype="int")
    for sent in word_input:
        text1 = re.sub('<s>|</s>', ' ', sent)
        text2 = text1.lower().strip().split()
        for word in text2:
            if word in word_index_dict_input:
                count_vector[word_index_dict_input[word]] = count_vector[word_index_dict_input[word]] + 1
    return count_vector


print(count_word(brown, word_index_dict))

vector_count = count_word(brown, word_index_dict)

probs = (vector_count / np.sum(vector_count))

print(probs[0])
print(probs[-1])

# vocab = open("brown_vocab_100.txt")
#
# #load the indices dictionary
# word_index_dict = {}
# for i, line in enumerate(vocab):
#     #TODO: import part 1 code to build dictionary
#
# f = open("brown_100.txt")
#
# counts = #TODO: initialize counts to a zero vector
#
# #TODO: iterate through file and update counts
#
# f.close()

# TODO: normalize and writeout counts.
