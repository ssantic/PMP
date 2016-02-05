class MyEnumerate(object):
    def __init__(self, numerator):
        self.numerator = numerator
        self.idx = 0

    def next(self):
        if self.idx >= self.len(self.numerator):
            raise StopIteration
        value = (self.idx, self.numerator[self.idx])
        self.idx += 1
        return value

    def __iter__(self):
        return self

for index, letter in MyEnumerate('abc'):
    print "{}:{}".format(index, letter)
