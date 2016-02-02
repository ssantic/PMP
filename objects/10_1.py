class Scoop(object):
    def __init__(self, flavor):
        self.flavor = flavor

s1 = Scoop('vanilla')
s2 = Scoop('chocolate')
s3 = Scoop('hazelnut')

scoops = [s1, s2, s3]

for scoop in scoops:
    print scoop.flavor
