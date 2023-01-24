li = [1, 1, 43, 2, 6, 542, 12, 2, 2134, 43, 2]

# Sort the list
for i in range(len(li)):
    for j in range(len(li)):
        if li[i] < li[j]:
            a = li[i]
            li[i] = li[j]
            li[j] = a

# print(li)

# Sort the list with sorted method
# Sorted function return a new list
my_list = [123, 23, 54, 325, 6, 34, 61, 42, 33, 41, 123, 4, 354]

my_list = sorted(my_list)
# print(my_list)

# sort() method sort the list and return None
my_list = [123, 23, 54, 325, 6, 34, 61, 42, 33, 41, 123, 4, 354]
my_list.sort()
# print(my_list)

# Sort the list in reverse
my_list.sort(reverse=True)
# print(my_list)

my_list = [123, 23, 54, 325, 6, 34, 61, 42, 33, 41, 123, 4, 354]
my_list = sorted(my_list, reverse=True)
# print(my_list)


# Let's sort a tuple
tup = (1, 4, 3, 1, 23, 54667, 121)
new_tup = sorted(tup)
# print(new_tup)


my_dict = {'name': 'arid', 'job': 'Becoming a programmer :(', 'age': 19}
# print(my_dict)
# Sorted function will sort the keys and will return a list
my_dict = sorted(my_dict)
# print(type(my_dict))

my_list.clear()
# Sort a list based on their absolute values
my_list = [-6, -5, -4, 1, 3, 2, 2, 3]

my_list.sort(key=abs)
print(my_list)


# Sort the objects

class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '{},{},${}'.format(self.name, self.age, self.salary)


emp1 = Employee('Carl', 37, 70000)
emp2 = Employee('Sarah', 29, 80000)
emp3 = Employee('John', 43, 90000)

employees = [emp1, emp2, emp3]


# If we try to sort the objects without any key in the sort method
# Python will throw an exception
# So to sort objects of a class we need to specify a key

def emp_sort_name(emp):
    return emp.name


def emp_sort_age(emp):
    return emp.age


def emp_sort_salary(emp):
    return emp.salary


employees.sort(key=emp_sort_age)

print(employees)

# If we want to sort objects in reverse

employees.sort(key=emp_sort_salary, reverse=True)

print(employees)
