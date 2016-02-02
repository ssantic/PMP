class Scoop(object):
    def __init__(self, flavor):
        self.flavor = flavor


class Cone(object):
    def __init__(self):
        self.scoops = []

    def add_scoops(self, *scoop_list):
        for s in scoop_list:
            if len(self.scoops) == 3:
                pass
            else:
                self.scoops.append(s)
        return self.scoops

    def __str__(self):
        return '\n'.join(scoop.flavor for scoop in self.scoops)

s1 = Scoop('vanilla')
s2 = Scoop('chocolate')
s3 = Scoop('hazelnut')
s4 = Scoop('strawberry')
s5 = Scoop('lime')

c = Cone()
c.add_scoops(s1, s2)
c.add_scoops(s3)
c.add_scoops(s4)
c.add_scoops(s5)
print(c)
