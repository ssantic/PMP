from collections import Counter

# Helper function to count the most repeating letter in a word
def most_repeating_letter_count(word):
	letter_count = Counter()
	for letter in word:
		letter_count[letter] += 1
	return letter_count[max(letter_count)]

def most_repeating_word(words):
    top_words = {}
    for word in words:
	    top_words[word] = most_repeating_letter_count(word)
    return max(top_words, key = top_words.get)

print most_repeating_word(['this', 'is', 'a', 'test', 'program'])