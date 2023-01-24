class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f'{self.first}.{self.last}@company.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # __repr__ repr(instance)
    # It is used for logging debugging and things like that

    def __repr__(self):
        pass

    # __str__ str(instance)
    # More readable representation of object
    def __str__(self):
        return '{}-{}'.format(self.first, self.last)

    # Will add pay of self instance and other instance
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


dev = Employee('arid', 'devops', 200)
dev1 = Employee('arid1', 'devops1', 250)
print(dev)
print('Pay: ')
print(dev + dev1)

# All types use dunder methods
print(1 + 2)
print(int.__add__(1, 2))
print(float.__add__(1.0, 2.0))
print(str.__add__('a', 'b'))

print(len('python for ai'))
print('python for ai'.__len__())
# Let call the len function into our instance
# First we need to create a __len__() method in our class
print('Length of full name: ' + str(len(dev)))
