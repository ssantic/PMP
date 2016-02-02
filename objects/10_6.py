class Cage(object):
    def __init__(self, cage_id):
        self.cage_id = cage_id
        self.animals = []

    def add_animals(self, *anims):
        for anim in anims:
            self.animals.append(anim)

    def __str__(self):
        return '\n'.join(str(animal) for animal in self.animals)
