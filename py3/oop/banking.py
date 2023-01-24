# Banking SYstem using OOP
# Parent Class: User
# Holds details about an user
# Has a function to how user details
# Child Class : Bank
# Stores details about account balance
# Stores details about the amount
# Allows for deposits, withdraw, view_balance


from codecs import namereplace_errors


class User:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, age):
        self.__name = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        self.__gender = gender

    def show_details(self):
        print(f"Name={self.__name}, age={self.__age} gender={self.__gender}")


# Child class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount
        print("Balance has been updated : 💲", self.__balance)

    def withdraw(self, amount):
        if self.__balance < amount:
            print("Not enough money to withdraw")
            return

        self.__balance -= amount
        print("Balance has been updated: 💲", self.__balance)

    def view_balance(self):
        self.show_details()
        print("Balance is : 💲", self.__balance)

"""
user = Bank(name='Aridon', age=20, gender='male')
user.deposit(200)
user.deposit(20)
user.withdraw(240)
user.view_balance()
"""


class Room:

    def __init__(self, name,floor):
        self.name = name
        self.floor = floor


    def __str__(self):
        return self.name


class RoomForm:

    def __init__(self, name,floor):
        self.name = name
        self.floor = floor

    def __str__(self):
        return self.name





room = Room(name='room one', floor='1')
room_form = RoomForm(instance=room)
print(room_form.name)
print(room_form.floor)
