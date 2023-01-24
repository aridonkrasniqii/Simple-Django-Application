def my_function():
    print('Hello from a function')


my_function()


def my_function(name):
    print(f'Hello {name} from a function ')


my_function('aridon')


# spread operator

def my_function(*argument):
    for i in argument:
        print(f'Hello {i} from a function')


my_function('aridon', 'kransiqi')


def my_function(arg1, arg2, arg3):
    print('The youngest child is ' + arg3)


my_function(arg1='aridon', arg2='aridon', arg3='aridon3')

"""
    Arbitrary Keyword Arguments, **kwargs 
    If you dont know how many keyword arguments that will be passed into a function, add two asterisk ** before the parameter
    name in the function definition 
    
    This way the function will receive a dictionary of arguments, and can access the items accordingly 
    
"""


def my_function(**kid):
    print('His last name is ' + kid['lname'])


my_function(fname='Tobis', lname='Smith')


# Default parameters
def my_function(country='Norway'):
    print('I am from ' + country)


my_function('Albani')
my_function()


# Passing list as an argument


def my_function(food):
    for i in food:
        print(i)


fruits = ['apple', 'pear', 'orange']

my_function(fruits)


# Recursion
def recursion(n):
    if n < 1:
        return 1
    else:
        return n * recursion(n - 1)


print(recursion(5))
