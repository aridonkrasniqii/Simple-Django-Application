class Person:

    def __init__(self):
        pass


person = Person()

first_key = 'first'
setattr(person, first_key, 'Corey')
print(person.first)

second_key = 'second'

setattr(person, second_key, 'Second')
print(person.second)

first = getattr(person, first_key)
print(first)


class User:

    def __init__(self, name):
        self.name = name


user = User('aridon')

name = getattr(user, 'name')
print(name)

"""person_info = {'first': 'Corey', 'last': 'Schafer'}

for key, value in person_info.items():
    setattr(person ,key ,value)
"""

import json


class Book:

    def __str__(self):
        return f"Book: {self.id} {self.language} {self.edition} {self.author} "


books = None
with open('json_file.json', 'r') as file:
    book_info = json.load(file).get('book')[0]

book = Book()
for attribute, value in book_info.items():
    setattr(book, attribute, value)

print(book)
print(book.id)


from getpass import getpass

username = input('Username ')
password = getpass('Password ')

print("Logging In...")



