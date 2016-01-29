import json
import os
import numpy

files = []
for file in os.listdir('C:/PMP/files/scores/'):
	files.append('C:/PMP/files/scores/' + file)

for file in files:
	f = open(file)
	scores = json.load(f)
	science = []
	literature = []
	math = []
	for i in xrange(len(scores)):
		science.append(scores[i]['science'])
		literature.append(scores[i]['literature'])
		math.append(scores[i]['math'])
	print file
	print '    science: min ' + str(min(science)) + ', max ' + str(max(science)) + ', average ' + str(numpy.mean(science))
	print '    literature: min ' + str(min(literature)) + ', max ' + str(max(literature)) + ', average ' + str(numpy.mean(literature))
	print '    math: min ' + str(min(math)) + ', max ' + str(max(math)) + ', average ' + str(numpy.mean(math))