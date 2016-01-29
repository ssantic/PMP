f = open('C:/PMP/files/passwd.txt')

lines = f.readlines()

result = {}

for i in xrange(len(lines)):
	key = lines[i].split(":")[0]
	value = lines[i].split(":")[2]
	result[key] = value

for key in result.keys():
	print key, "   ", result[key]