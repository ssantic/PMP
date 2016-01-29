import csv

csvfile = open('C:/PMP/files/passwd.csv', 'r')
lines = csv.reader(csvfile, delimiter = '\t', quoting = csv.QUOTE_NONE)
result = {}

for row in lines:
	if row[0][0] != '#':
		row_split = row[0].split(':')
		result[row_split[0]] = row_split[2]

csv_result = open('6_5_result.csv', 'wb')
writer = csv.writer(csv_result, delimiter = '\t')

for key, value in result.items():
   writer.writerow([key, value])