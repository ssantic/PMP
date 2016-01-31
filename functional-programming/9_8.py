def gematria_dict():
	import string
	result = {}
	for i in xrange(len(string.ascii_lowercase)):
		result[string.ascii_lowercase[i]] = int(i+1)
	return result


def gematria_value(word):
	value = 0
	for letter in word:
		value += gematria_dict()[letter]
	return value


def matching_gematria(word, dict_path):
	dictionary = open(dict_path)
	lines = dictionary.read().splitlines()
	match_value = gematria_value(word)
	matching_words = []
	for line in lines:
		if gematria_value(line) == match_value:
			matching_words.append(line)
	return matching_words


print matching_gematria('cat', 'C:/PMP/functional-programming/dictionary.txt')