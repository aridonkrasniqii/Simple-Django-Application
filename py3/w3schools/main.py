print(int(1))
print(int('2'))
print(int(2.2))
string = """
l;aknsdlkasdash dasd asd
asd
"""
print(string)
b = 'Hello World'
print(b[2:5])
print(b[:5])

print(b[-5:-2])
print(b.upper())
print(b.lower())
print(b.capitalize())
print(len(b))
b = 'Hello,World'
# remove the whitespaces
print(b.strip())
print(b.replace('H', 'aridon'))
print(b.split(','))
b = b.split(',')
b = ','.join(b)
print(b)
a = 'Hello '
b = 'World'
print(a, b)
print(a + b)
print(f'{a} {b}')
print('{} {}'.format(a, b))
quantity = 100
price = 49.95
item_no = 567
my_order = 'I want {} pieces of the item {} for {} dollars '
print(my_order.format(quantity, item_no, price))
print(my_order.find('want'))
print(my_order.index('want'))
print(my_order.count('want'))
print(my_order.islower())
print(my_order.islower())
print(my_order.isupper())
print(10 == 2)
print(10 < 12 < 22)
print(bool('hello'))
print(bool(1))
print(bool('2'))
print(bool({1, }))

programming_lang = ['java', 'python', 'c++', 'javascript']

programming_lang.insert(len(programming_lang) + 1, 'docker')
print(programming_lang)

a = [1, 2, 3]
b = [2, 3, 4, 4]
a = a + b
print(a)
a = [1, 2, 3]
a.extend(b)
print(a)
a.remove(1)
print(a)
a.pop(0)
print(a)
del a[0]
print(a)
a.clear()
print(a)
print(bool(a))
a = [1, 2, 2, 312, 3, 123, 12, 3]
for value in a:
    print(value, end=' ')
print()
for index in range(len(a)):
    print(a[index], end=' ')
print()

i = 0
while i < len(a):
    print(a[i], end=' ')
    i += 1

print()
[print(x, end=' ') for x in a]
print()
print(''.join(str(a)))

fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mongo']
new_list = []
[new_list.append(fruit) for fruit in fruits]
print(new_list)
new_list.clear()
for fruit in fruits:
    new_list.append(fruit)

print(new_list)

fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mongo']

new_list = [x for x in fruits]
new_list.clear()
new_list = [fruits[index] for index in range(len(fruits))]
print(new_list)

new_list.clear()
new_list = [x for x in fruits if x != 'apple']
print(new_list)
new_list.clear()
# change banana with orange
new_list = [x if x != 'banana' else 'orange' for x in fruits]
print(new_list)
new_list.sort()
print(new_list)
new_list.reverse()
print(new_list)
new_list.reverse()
print(new_list)
new_list.sort(reverse=True)
print(new_list)
new_list[1] = new_list[1].upper()
new_list.sort(key=str.lower)
print(new_list)
new_list.clear()
new_list = fruits.copy()
print(new_list)
a, b, *c = new_list
print(a, b, c)


def my_func():
    print("Hello from a function ")


my_func()

add_10 = lambda x: x + 10
print(add_10(20))
multy = lambda x, y: x * y
print(multy(2, 2))


# ax^2 + bx + c
def my_func(x):
    return lambda a, b, c: a * x ** 2 + b * x + c


quadratic = my_func(2)
print(quadratic(1, 2, 3))
print(quadratic(22, 3, 3))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is {}".format(self.name))


p1 = Person('aridon', 20)
print(p1.name, p1.age)
p1.myfunc()


class Person():

    def __init__(myobj, name, age):
        myobj.name = name
        myobj.age = age

    def myfunc(self):
        print("Hello my name is {}".format(self.name))


p1 = Person(name='aridon', age=20)
p1.myfunc()


class Person():

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print("My name is {} {}".format(self.firstname, self.lastname))


p1 = Person('aridon', 'kransiqi')
print(p1.firstname)
print(p1.lastname)
p1.printname()


class Student(Person):

    def __init__(self, fname, lname, avg_grade, teacher):
        super().__init__(fname, lname)

        self.avg_grade = avg_grade
        self.teacher = teacher

    def printname(self):
        return super().printname()

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, ' to the class of ', self.teacher)


student_dict = {'fname': 'aridon', 'lname': 'kransiqi', 'avg_grade': 9.55, 'teacher': "The cherno"}
student = Student(**student_dict)
print(student.avg_grade)
student.printname()
student.welcome()

mytuple = ('apple', 'banana', 'cherry', 'strawberry')
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

mystr = 'banana'
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

mytuple = ('banana', 'apple', 'cherry', 'blueberry')

for x in mytuple:
    print(x)

mystr = 'banana'

for letter in mystr:
    print(letter)


class Iter():

    def __init__(self, value):
        self.value = value

        if isinstance(self.value, str):
            self.value = [x for x in self.value]

    def __next__(self):
        if isinstance(self.value, tuple):
            self.value = list(self.value)
        value = self.value[0]
        self.value.pop(0)
        self.value = tuple(self.value)
        return value


mytuple = Iter(('banana', 'apple', 'cherry', ' strawberry'))

print(next(mytuple))
print(next(mytuple))
print(next(mytuple))
print(next(mytuple).strip())

import json

json_string = """
     {    
        "fname" :"Aridon",
        "lname" :"Krasniqi",
        "age" : 36 ,
        "country" : "Kosovo"
     }
"""

json_data = json.loads(json_string)

print(json_data)

del json_data['age']

json_string = json.dumps(json_data, indent=4)

print(json_string)
for key , value in json.loads(json_string).items():
    print(key, "=", value)



f = open('demofile.txt', 'r')


print(f.read())

print("\n\n\n Second read")
with open('demofile.txt', 'r') as file:
    size_to_read = 100
    content = file.read(size_to_read)
    while len(content) > 0:
        print(content)
        content = file.read(size_to_read)




import os
os.system("cp demofile.txt file.txt")

os.remove('demofile.txt')

if os.path.exists('demofile.txt'):
    print("File is not deleted")
else:
    print("Files in this directory: " , os.listdir(os.curdir))