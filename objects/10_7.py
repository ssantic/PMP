class Cage(object):
    def __init__(self, cage_id):
        self.cage_id = cage_id
        self.animals = []

    def add_animals(self, *anims):
        for anim in anims:
            self.animals.append(anim)

    def __str__(self):
        return '\n'.join(str(animal) for animal in self.animals)

    def animals_by_color(self, color):
        return '\n'.join(str(animal) for animal in self.animals
                         if animal.color == color)

    def animals_by_legs(self, legs):
        return '\n'.join(str(animal) for animal in self.animals
                         if animal.legs == legs)

    def legs(self):
        return sum(animal.legs for animal in self.animals)


class Zoo(object):
    def __init__(self):
        self.cages = []

    def add_cages(self, *cages):
        for cage in cages:
            self.cages.append(cage)

    def __str__(self):
        '\n'.join(str(cage) for cage in self.cages)

    def animals_by_color(self, color):
        '\n'.join(cage.animals_by_color(color) for cage in self.cages)

    def animals_by_legs(self, legs):
        return '\n'.join(cage.animals_by_legs(legs) for cage in self.cages)

    def legs(self):
        return sum(cage.legs for cage in self.cages)
