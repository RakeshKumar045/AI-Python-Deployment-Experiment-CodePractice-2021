import json

# charset=utf-16le

with open('brown_vocab_100.txt', encoding='utf-16') as f:
	contents = f.read()

final = contents.rstrip().replace('\n', ' ').split(' ')

# create dict
word_index_dict = {}
for i, a in enumerate(final):
	word_index_dict[a] = i
# print(i, a)

with open('word_to_index_100.txt', 'w') as file:
	file.write(json.dumps(word_index_dict))

# TODO: read brown_vocab_100.txt into word_index_dict

# TODO: write word_index_dict to word_to_index_100.txt


print(word_index_dict['all'])
print(word_index_dict['resolution'])
print(len(word_index_dict))
