# One  value to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a collection
my_list = ['Phone', 'Laptop', 'Pc', 'IPad']
phone, laptop, pc, ipad = my_list
print(phone)
print(laptop)

# Print multiple variables
print(phone, pc, ipad)

# Print with + operator
print(phone + pc + ipad)

# Global variables - variables that are declared outside of a function
x = 'awesome'


def myfunc():
    print('Python is ' + x)


myfunc()

# Global variable
"""
    If you create a variable with the same name inside a function, 
    this variable will be local,and can only be used inside the function
    
"""
x = "awesome"


def myfunc():
    x = 'fantastic'
    print('Pythin is  ' + x)


myfunc()
print('Python is ' + x)

# global Keyword
x = 'fantastic'


def myfunc():
    global x
    x = 'awesome'


myfunc()

print('Python is ' + x)
