def supervocalic(dict_path):
	dictonary = open(dict_path)
	lines = dictonary.readlines()
	result = []
	for line in lines:
		if 'a' and 'e' and 'i' and 'o' and 'u' in line:
			result.append(line)
	return result


print supervocalic('C:/PMP/functional-programming/dictionary.txt')