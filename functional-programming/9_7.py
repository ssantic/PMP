def gematria_dict():
	import string
	result = {}
	for i in xrange(len(string.ascii_lowercase)):
		result[string.ascii_lowercase[i]] = int(i+1)
	return result

print gematria_dict()