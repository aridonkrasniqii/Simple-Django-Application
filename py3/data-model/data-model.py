# dunder methods double underscore methods or data model
# objects

# add -> __add__
# initialize -> __init__
# repr(x) -> __repr__
# length -> __len__
# x() -> __call__

class Polynomial:

    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return 'Polynomial(*{!r})'.format(self.coeffs)

    def __add__(self, other):
        return [x + y for x, y in zip(self.coeffs, other.coeffs)]

    def __len__(self):
        return len(self.coeffs)


    def __call__(self):
        return self.coeffs[1]

p1 = Polynomial(1, 2, 3)
p2 = Polynomial(3, 4, 3)
print(p1.coeffs)

print(p1 + p2)

print(len(p1))
print(len(p2))
print(p1())
