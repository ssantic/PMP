def mysum(*items):
	if not items:
		return items
	output = type(items)()
	for item in items:
		output += item
	return output

print mysum('abc', 'def')
print mysum([1,2,3], [4,5,6])
print mysum(1,2,3)