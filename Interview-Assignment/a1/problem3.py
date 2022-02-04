import numpy as np
from sklearn.preprocessing import normalize

word_index_dict = {}

with open("brown_vocab_100.txt") as f:
    vocab = [line.rstrip('\n') for line in f]

for ind, word in enumerate(vocab):
    word_index_dict[word] = ind

print(word_index_dict)

with open("brown_100.txt") as f:
    brown = [line.rstrip('\n') for line in f]


def generate_combination_word(previous, brown_text):
    dic_word_count = {}
    total_count = 0

    for sent in brown_text:
        text = sent.lower().strip().split()
        for word in text:
            if not (previous, word) in dic_word_count:
                dic_word_count[(previous, word)] = 1
                previous = word
            else:
                dic_word_count[(previous, word)] += 1
                previous = word
                total_count += 1

    dic_index_word = {}
    count = 0

    for i, v in dic_word_count.items():
        dic_index_word[count] = i
        count = count + 1

    return dic_word_count, dic_index_word, total_count


def count_matrix(dic_word_count_val, dic_index_word_val, total_count_val):
    array_count_matrix = np.zeros([len(dic_index_word_val), 2])

    for i in range(0, len(dic_index_word_val)):
        array_count_matrix[i][0] = int(i)
        array_count_matrix[i][1] = dic_word_count_val[dic_index_word_val[i]] / total_count_val

    return array_count_matrix


prev = '<s>'
dic_word_count_value, dic_index_word_value, total_count_value = generate_combination_word(prev, brown)

print("*" * 100)
print(dic_word_count_value)
print("*" * 100)

print(dic_index_word_value)
print("*" * 100)

count = count_matrix(dic_word_count_value, dic_index_word_value, total_count_value)

print(count)
print("*" * 100)

probs = normalize(count, norm='l1', axis=1)

print(probs)
print("*" * 100)

prob = dic_word_count_value[('all', 'the')] / total_count_value


def save_dict_to_file(prob):
    f = open('bigram_probs.txt', 'w')
    f.write(str(prob))
    f.close()


save_dict_to_file(prob)

f.close()

# vocab = codecs.open("brown_vocab_100.txt")
#
# #load the indices dictionary
# word_index_dict = {}
# for i, line in enumerate(vocab):
#     #TODO: import part 1 code to build dictionary
#
# f = codecs.open("brown_100.txt")


counts = ""  # TODO: initialize numpy 0s array

# TODO: iterate through file and update counts

# TODO: normalize counts


# TODO: writeout bigram probabilities
