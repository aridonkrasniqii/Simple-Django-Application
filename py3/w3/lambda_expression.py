"""
 A lambda function is a small anonymous function
 A lambda function can take any number of arguments, but can only have one expression

"""


# Syntax
# lambda arguments : expression

# Example
def add(a):
    return a + 10


print(add(5))

# With lambda expression
# 1.
x = lambda a: a + 10
print(x(5))

# 2.
x = lambda a, b: a * b
print(x(10, 10))

# 3.
x = lambda a, b, c: a + b + c
print(x(1, 2, 3))

""" 
    Why use lambda functions 
    The power of lambda is better  shown when you use them as an 
    anonymous function inside another function 
    Say you have a function definition that takes one argument, 
    and that will be multiplied with an unknown number: 
    
"""


def my_function(n):
    return lambda a: a * n


my_doubler = my_function(2)

print(my_doubler(10))


# Example with triples


def my_function(n):
    return lambda a: a * n


my_tripler = my_function(3)

print(my_tripler(10))


# quadratic function
# f(x) = ax^2 + bx + c

def quadratic_function(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


f = quadratic_function(1, 2, 3)

print(f(10))
