numbers = str(raw_input("Please enter an array of integers, all at once: "))

result = 0

for i in xrange(len(numbers)):
	result += int(numbers[i])

print result