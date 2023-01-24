# Dunder -> means double underscore __

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print('Object is being deconstructed')


p = Person("Mike", 25)
# Deconstruct the object with del function
# You need to create method __del__ in class
# PS:
# If you don't call the method del the object will be deconstructed at the end of the program
# If you call the method the object will be deconstructed immediately
del p


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        pass

    def __repr__(self):
        return f'{Vector.__name__} x = {self.x}  , y = {self.y}'

    def __len__(self):
        return 10

    def __call__(self, *args, **kwargs):
        print('Hello! I was called! ')


v1 = Vector(10, 20)
v2 = Vector(50, 60)
# if we want to add these two objects together you need to implement __add__ method
v3 = v1 + v2

print(f'{Vector.__name__} v3.x = {v3.x} v3.y = {v3.y}')
print(v3)
print(len(v3))
v3() # call method