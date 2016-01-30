input_file = open('C:/PMP/files/sample.mdown')

lines = input_file.readlines()

output_file = open('C:/PMP/files/exercises.md', 'a')

output_file.write('%s\n' % ('# Exercises'))
output_file.write('%s\n' % (''))
output_file.write('%s\n' % ('## Filename'))
output_file.write('%s\n' % (''))

line_counter = 0
for i in xrange(len(lines)):
	if lines[i][1] == '#' and lines[i][2] != '#':
		line_counter += 1
		output_file.write('%s\n' % ('### ' + str(line_counter) + '. ' + lines[i][3:]))
		output_file.write('%s\n' % (lines[i+1]))