class Scoop(object):
    def __init__(self, flavor):
        self.flavor = flavor


class Cone(object):
    max_scoops = 3

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *scoop_list):
        for s in scoop_list:
            if len(self.scoops) == self.max_scoops:
                pass
            else:
                self.scoops.append(s)
        return self.scoops

    def __str__(self):
        return '\n'.join(scoop.flavor for scoop in self.scoops)


class BigCone(Cone):
    max_scoops = 5


s1 = Scoop('vanilla')
s2 = Scoop('chocolate')
s3 = Scoop('hazelnut')
s4 = Scoop('strawberry')
s5 = Scoop('lime')

b = BigCone()
b.add_scoops(s1, s2)
b.add_scoops(s3)
b.add_scoops(s4, s5)
print(b)
