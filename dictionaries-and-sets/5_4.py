def dictdiff(dict_1, dict_2):
	result = {}
	all_keys = set(dict_1.keys())
	all_keys.update(dict_2.keys())

	for key in all_keys:
		if dict_1.get(key) != dict_2.get(key):
			result[key] = [dict_1.get(key), dict_2.get(key)]

	return result


d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'c':4}
print dictdiff(d1,d2)

d3 = {'a':1, 'b':2, 'd':3}
d4 = {'a':1, 'b':2, 'c':4}
print dictdiff(d3,d4)

d5 = {'a':1, 'b':2, 'c':3}
d6 = {'a':1, 'b':2, 'd':4}
print dictdiff(d5,d6)