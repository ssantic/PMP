def flatten(input_list):
	result = []
	for element in input_list:
		if len(element) > 1:
			for e in element:
				result.append(e)
		else:
			result.apend(element)
	return result

print flatten([[1,2], [3,4]])