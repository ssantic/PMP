numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

result = []

[result.append((str(number) + ',')) if number != numbers[-1] else result.append(str(number)) for number in numbers]

result = ''.join(result)

print result

"""

for number in numbers:
	if number != numbers[-1]:
		result += str(number)
		result += ','
	else:
		result += str(number)

"""