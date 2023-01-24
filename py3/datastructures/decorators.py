def outer_func(msg):
    def inner_func():
        print(msg)

    # return inner_func()
    # return the function without executing it
    return inner_func


# my_func is going to be equal to our function
bye_func = outer_func('Bye')
hi_func = outer_func('Hi')

# Decorator is a function that takes another function as an argument , add some kind of functionality and returns a
# function
"""
def decorator_function(message):
    def wrapper_function():
        print(message)

    return wrapper_function
"""


def decorator_function(original_function):
    def wrapper_function():
        return original_function()

    return wrapper_function


def display():
    print('Display function ran')


decorated_display = decorator_function(display)

decorated_display()

"""
    Real example
     
    Instead of using this syntax to create decorators
    ***
        def display():
        print('display function ran')
        decorated_display = decorator_example(display)
        decorated_display()
    ***
    We use this syntax
"""


def decorator_example(original_function):
    def wrapper_function():
        print('Wrapper executed this before {}'.format(original_function.__name__))
        return original_function

    return wrapper_function


@decorator_function
def display():
    print('Display function ran')


display = decorator_example(display)


def decorator_function(original_func):
    def wrapper_function(*args, **kwargs):
        print('Inner function executed by {}'.format(original_func.__name__))
        return original_func(*args, **kwargs)

    return wrapper_function


@decorator_function
def display_info(name, age):
    print('Display info ran with arguments ({} {})'.format(name, age))


display_info(name='arid', age=20)


class decorator_class(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)



@decorator_class
def display():
    print('display function ran')



@decorator_class
def display_info(name, age):
    print('display info ran with arguments ({} {})'.format(name,age))