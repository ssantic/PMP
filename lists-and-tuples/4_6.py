people = [('Barack', 'Obama', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]

for i in xrange(len(people)):
    print people[i][1] + ' '*(10-len(people[i][1])) + ' ' + people[i][0] + ' '*(10-len(people[i][0])) + ' ' + str(round(people[i][2], 2)) + ' '*(5-len(str(round(people[i][2], 2))))
