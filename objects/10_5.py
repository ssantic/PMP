class Animal(object):
    def __init__(self, color):
        self.color = color
        self.species = self.__class__.__name__

    def __str__(self):
        return "%s %s, %s" % (self.color, self.species, self.legs)


class Sheep(Animal):
    legs = 4


class Wolf(Animal):
    legs = 4


class Snake(Animal):
    legs = 0


class Parrots(Animal):
    legs = 2


s = Sheep('white')

print s.color
print s.species
print s.legs
print(s)
