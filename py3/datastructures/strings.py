from datetime import datetime

person = {'name': 'Jenn', 'age': 23}
sentence = 'My name is {} and I am {} years old'.format(person['name'], person['age'])
print(sentence)

tag = 'h1'
text = "This is a headline"
sentence = '<{0}>{1}</{0}>'.format(tag, text)
print(sentence)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('arid', 19)
sentence = 'My name is {0.name} and I am {0.age} years old .'.format(p1)
print(sentence)

# We can also pass in keyword arguments
sentence = 'My name is {name} and I am {age} years old '.format(name='arid', age=19)
print(sentence)

# Example with unpacking
person = {'name': 'arid', 'age': 19}
# **person will unpack the dictionary
sentence = "My name is {name} I am {age} years old".format(**person)
print(sentence)

for i in range(10):
    print('Value is {} '.format(i))

# Format string
# 0 stands for the first number if the format is one digit is like a fill number
# 2 stands for number of digits to be displayed
for i in range(1, 11):
    print('The value is {:02}'.format(i))

pi = 3.14159265
sentence = "Pi is equal to {}".format(pi)
print(sentence)

sentence = "1 MB is equal to {} bytes".format(2 ** 20)
print(sentence)

sentence = "1 MB is equal to {:,} bytes".format(2 ** 20)
print(sentence)

# 2 digits after the comma
sentence = "1 MB is equal to {:.2f} bytes".format(2 ** 20)
print(sentence)

sentence = "1 MB is equal to {:,.2f} bytes ".format(2 ** 20)
print(sentence)

# Current date time in local system
my_date = datetime.now()

