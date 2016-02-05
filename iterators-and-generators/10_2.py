class Circle(object):
    def __init__(self, sequence, n):
        self.sequence = sequence
        self.n = n
        self.idx = 0

    def next(self):
        if self.idx >= self.n:
            raise StopIteration
        value = self.sequence[self.index % len(self.sequence)]
        self.index += 1
        return value

    def __iter__(self):
        return self
