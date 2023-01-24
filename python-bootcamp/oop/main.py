# from abc import ABC, abstractmethod
#
#
# class User(ABC):
#
#     def __init__(self, ssn, fname, lname):
#         self.__ssn = ssn
#         self.__fname = fname
#         self.__lname = lname
#
#     @abstractmethod
#     def print_details(self):
#         pass
#
#     @property
#     def ssn(self):
#         return self.__ssn
#
#     @property
#     def fname(self):
#         return self.__fname
#
#     @property
#     def lname(self):
#         return self.__lname
#
#
# class Accountant(User):
#
#     def __init__(self, ssn, fname, lname, salary):
#         super().__init__(ssn, fname, lname)
#         self.__salary = salary
#
#     def __repr__(self):
#         return f"Accounant ({self.ssn} , '{self.fname}' ,'{self.lname}', {self.__salary}) "
#
#     def print_details(self):
#         print(self)
#
#
# acc = Accountant(ssn=1, fname='aridon', lname='krasniqi', salary=2000)
# acc.print_details()
#
#
# class CostumException(Exception):
#
#     def __init__(self, msg):
#         self.msg = msg
#
#     def print_exception(self):
#         print("User defined exception: ", self.msg)
#
#
# try:
#     raise CostumException("Exception is thrown! ")
# except CostumException as s:
#     s.print_exception()
#
# """
# import argparse
#
# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument("number1", help="first number")
#     parser.add_argument("number2", help="second number")
#     parser.add_argument("number3", help="third number")
#
#     args = parser.parse_args()
#
#     print(args.number1)
#     print(args.number2)
#     print(args.number3)
# """
#
# import time
#
# """
# def calc_square(numbers):
#     start_time = time.time()
#     for num in numbers:
#         yield num * num
#
#     end_time = time.time()
#     print('Calc_square took ' , ((end_time - start_time) * 1000) , ' mil sec')
#
#
#
#
# def calc_cube(numbers):
#     start_time = time.time()
#     result = []
#     for num in numbers:
#         result.append(num ** 3)
#     end_time = time.time()
#     print("Calc_cube took ", ((end_time - start_time) * 1000), " mil sec")
#     return result
#
#
# numbers = [1, 2, 3, 4, 5, 6, 7]
#
# numbers = list(calc_square(numbers))
#
# print(numbers)
# numbers = calc_cube(numbers)
# print(numbers)
# """
#
#
# def time_it(function):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = function(*args, **kwargs)
#         end_time = time.time()
#         print(f"{function.__name__} took {((end_time - start_time) * 1000)} mil sec")
#         return result
#
#     return wrapper
#
#
# @time_it
# def calc_square(numbers):
#     result = []
#     for num in numbers:
#         result.append(num ** 2)
#     return result
#
#
# print(calc_square([1, 2, 3, 4, 5, 6, 7]))
#
#
# def implement_threading():
#     print("First string")
#     time.sleep(5)
#     print("Second string")
#
#
# import threading
#
# for _ in range(10):
#     thread1 = threading.Thread(target=implement_threading)
#     thread1.start()
#
nums = [1, 2, 3, 4, 5, 6, 7]

my_list = []

for num in nums:
    my_list.append(num)

print(my_list)
my_list.clear()
my_list = [x for x in nums]
print(my_list)

my_list.clear()

my_list = list(map(lambda n: n * n, nums))

print(my_list)

my_list = list(filter(lambda x: x % 2 == 0, nums))
print(my_list)
my_list.clear()

my_list = [x for x in nums if x % 2 == 0]
print(my_list)

letters = 'abcd'
numbers = '1231'

combination = []
for index in range(len(letters)):
    combination.append((letters[index], numbers[index]))

print(combination)

# comprehension

combination.clear()

combination = [(letters[index], numbers[index]) for index in range(len(numbers))]
print(combination)

nums = [1, 2, 3, 4, 5]
combination.clear()

combination = [(letter, num) for letter in letters for num in range(len(letters))]

print(combination)

# dictionary comprehension


names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverien', 'Deadpool']

dict = {}

for name, hero in zip(names, heroes):
    dict[name] = hero

print(dict)

dict.clear()
dict = {name: hero for name, hero in zip(names, heroes) if name != 'Peter'}
print(dict)

# set comprehensions
nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 7, 8, 9]

my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)

my_set.clear()
my_set = {n for n in nums}
print(my_set)


# square numbers

def sqrt(numbers):
    for num in numbers:
        yield num * num


numbers = [x for x in range(11)]
print(list(sqrt(numbers)))

import collections
from collections import Counter

c = Counter('gallad')
print(c)
c = Counter(['a', 'b', 'c', 'd'])
print(c)
c = Counter({'a': 1, 'b': 2})
print(c)
c = Counter(dogs=6, cats=5)
print(c)

c = Counter(real=4, not_real=3)
print(list(c.elements()))

# how many elements you want to show
print(c.most_common(1))

from collections import namedtuple

Person = namedtuple('Person', ('fname', 'age', 'salary'))


person = Person(fname='aridon', age=20, salary=0)

print(person)
print(person.fname,person.age , person.salary)