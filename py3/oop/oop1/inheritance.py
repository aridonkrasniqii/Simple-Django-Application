"""
import datetime


class Math:

    @staticmethod  # means not changing , staying the same
    def add5(x):
        \"""
            all it is going to do is act like a function that is defined inside the class
            its more about organization thing , to organize functions

        :return:
        \"""
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10

    @staticmethod
    def pr():
        print('run')


print(Math.add5(5))
print(Math.add10(10))
print(Math.pr())

# r - IT will IGNORE ANY ESCAPE CHARACTER
\"""
r
string is
for file location.
    putting
    a
    r in front
    of
    a
    string
    means
    that
    the
    string is a
    file
    location
    / folder
    location
\"""

print(r'foo\\bar\n pool')

#
#
#
#
#
#
#
#
#
#
#
#
#
#

import csv


class Employee:
    raise_amount = 1.04
    num_of_emp = 0
    all = []

    def __init__(self, first, last, email, pay: int):
        self.first = first
        self.last = last
        self.email = email
        self.pay = pay
        Employee.num_of_emp += 1

        Employee.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__} ('{self.first}','{self.last}','{self.email}',{self.pay})"

    @classmethod
    def instantiate_from_csv(cls):
        with open('file.csv') as f:
            content = csv.DictReader(f)
            instantiated_obj = list(content)

        for obj in instantiated_obj:
            Employee(
                first=obj.get('first'),
                last=obj.get('last'),
                email=obj.get('email'),
                pay=obj.get('pay')
            )

    def fullname(self):
        print('{} {}'.format(self.first, self.last))

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, email, pay = emp_str.split('-')
        cls(first, last, email, pay)

    @staticmethod
    # The idea is to not use the instance or the class in the function

    def is_workday(day):
        if day.weekday() == 1 or day.weekday() == 6:
            return True
        else:
            return False


# emp1 = Employee('Corey', 'Schafer', 'coery@hotmail.com', 200)
# emp2 = Employee('user', 'user', 'user@hotmail.com', 200)

# emp1.fullname()
# Employee.fullname(emp1)
# If we call it with class name Employee.fullname(instance) we need to pass the instance as an argument
# If we call it with an instance the argument will be passed automatically


# information about attributes of instance .__dict__

Employee.set_raise_amount(1.05)
# print(emp1.__dict__)
# print(Employee.__dict__)
# print(emp1.num_of_emp)
# print(emp1.raise_amount)


instance_str = 'user3-user3-user3@outlook.com-200'

Employee.from_string(instance_str)

Employee.instantiate_from_csv()
print(Employee.all)

my_date = datetime.date(2016, 7, 10)
print(Employee.is_workday(my_date))
"""


class Employee:
    raise_amt = 1.04
    emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{self.first.lower()}.{self.last.lower()}@outlook.com'
        Employee.emps += 1

    def fullname(self):
        return '{}{}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return f"{self.__class__.__name__} ('{self.fullname()}' , '{self.email}' , {self.pay})"


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, programming_lang):
        super().__init__(
            first, last, pay
        )
        # You can do it like Employee.__init__(first,last,pay)
        self.programming_lang = programming_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(
            first, last, pay
        )
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)
        else:
            return False

    def del_emp(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
        else:
            return False

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp)


# help() function
# print(help(Developer))

dev1 = Developer('Arid', 'Developer', 5000, 'python')
dev2 = Developer('arid', 'developer', 5000, 'python')
dev3 = None
emp_list = []
emp_list[:] = [dev1, dev2, dev3]

manager = Manager('Manager', 'Manager', 500, emp_list)

dev4 = Developer('arid', 'devops', 100, 'python')

manager.add_emp(dev4)
manager.del_emp(dev3)
manager.print_emp()

# check if instance is instance of Employee and Developer
print(isinstance(dev1, Developer))
# function issubclass(Subclass Name, Superclass Name)

print(issubclass(Manager, Employee))
