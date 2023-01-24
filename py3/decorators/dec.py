
# dec.py
from time import time




class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.age = age


    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self, value):
        self.__name = value

    def __add__(self, other):
        return self.age + other.age

    def __repr__(self):
        return f"{self.__class__.__name__} ({self.name=}, {self.age=})  "






person1 = Person('Lorent', "Sinani' ", 50)
person2 = Person("Aridon", "KRasniqi", 12)
print(person2 + person1)


print(person1)






"""
def log(function):

    def wrapper(*args, **kwargs):
        with open('file.txt', 'w') as file:
            rv = function(*args, **kwargs)
            file.write(str(rv))
            return rv
    return wrapper

@log
def lorenti(x,  y):
    return x + y

lorenti(1, 2)


def timeit(function):
    def wrapper(*args , **kwargs):
        before = time()
        rv = function(*args , **kwargs)
        after = time()
        print('Elapsed time : , ' , (after - before) * 1000)
        return rv

    return wrapper


@timeit
def add(x , y= 10):
    return x + y










def sub(x, y = 10):
    return x - y





print('timeit(add(10))', timeit(add(10)))

print('add(10)', add(10))
print('add(20, 30)', add(20, 30))
print('add("a", "b")' , add("a", "b"))
"""