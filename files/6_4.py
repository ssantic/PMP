import os

def file_list(folder):
	files = []
	for file in os.listdir(folder):
		if file.endswith(".txt"):
			files.append(folder + "/" + file)
	return files


def longest_word(folder):
	text_files = file_list(folder)
	result = {}
	for text_file in xrange(len(text_files)):
		word_result = 'a'
		f = open(text_files[text_file])
		lines = f.readlines()
		for line in xrange(len(lines)):
 		    for word in lines[line].split():
				if len(word) > len(word_result):
					word_result = word					
		result[text_files[text_file]] = word_result
	return result


print longest_word('C:/PMP/files')