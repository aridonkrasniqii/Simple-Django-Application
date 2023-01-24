# Decorators add a certain functionality to a function


def my_decorator(function):
    def wrapper():
        print('I am decorating your function')
        function()

    return wrapper


def hello_world():
    print('Hello world')


# we are not doing this in python
# my_decorator(hello_world)()

wrapper = my_decorator(hello_world)
wrapper()


@my_decorator
def hello_world():
    print(f'Hello world')


hello_world()





""" ** Parameters ** """


def my_decorator(function):
    def wrapper(*args):
        print('I am decorating your function')
        function(*args)

    return wrapper


@my_decorator
def hello(person):
    print('hello {}'.format(person))


hello('mike')

