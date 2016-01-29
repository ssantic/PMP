def wc(file):
	f = open(file)
	lines = f.readlines()
	# Number of lines
	print "The file contains", len(lines), "lines."
	# Number of words
	word_number = 0
	for i in xrange(len(lines)):
		word_number += len(lines[i].split())
	print "The file contains", word_number, "words."
	# Number of characters
	char_number = 0
	for i in xrange(len(lines)):
		char_number += len(lines[i])
	print "The file contains", char_number, "characters, including whitespace."
	# Number of unique words
	words = []
	for i in xrange(len(lines)):
		line_words = lines[i].split()
		for j in xrange(len(line_words)):
			if line_words[j] not in words:
				words.append(line_words[j])
	print "The file contains", len(words), "unique words."


wc('C:/PMP/files/test-file.txt')