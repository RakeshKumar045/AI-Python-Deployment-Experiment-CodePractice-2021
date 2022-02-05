word_index_dict = {}

# TODO: read brown_vocab_100.txt into word_index_dict

# TODO: write word_index_dict to word_to_index_100.txt


with open("brown_vocab_100.txt") as f:
    vocab = [line.rstrip('\n') for line in f]

for ind, word in enumerate(vocab):
    word_index_dict[word] = ind


def save_dict_to_file(dic):
    f = open('word_to_index_100.txt', 'w')
    f.write(str(dic))
    f.close()


def load_dict_from_file():
    f = open('word_to_index_100.txt', 'r')
    data = f.read()
    f.close()
    return eval(data)


save_dict_to_file(word_index_dict)

word_index_dict = load_dict_from_file()

print(word_index_dict['all'])
print(word_index_dict['resolution'])
print(len(word_index_dict))
