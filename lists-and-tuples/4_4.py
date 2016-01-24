people = [{'first': 'Reuven', 'last': 'Lerner', 'email': 'reuven@lerner.co.il'},
          {'first': 'Barack', 'last': 'Obama',
              'email': 'president@whitehouse.gov'},
          {'first': 'Vladimir', 'last': 'Putin',
              'email': 'president@kremvax.ru'}
          ]

# http://stackoverflow.com/a/73050
people_sorted = sorted(people, key=lambda k: (k['last'], k['first']))

for i in xrange(len(people_sorted)):
    print people_sorted[i]['first'] + ", " + people_sorted[i]['last'] + ": " + people_sorted[i]['email']

