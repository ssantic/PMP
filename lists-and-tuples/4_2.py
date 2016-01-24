replacement = ['a', 'a', 'a', 'a', 'a', 'a']

def all_a(mylist):
	for i in xrange(len(mylist)):
		mylist[i] = replacement
	return mylist

print all_a([1,2,3])