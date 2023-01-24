# FIRST CLASS FUNCTIONS ALLOWS US TO TREAT FUNCTIONS
# LIKE ANY OTHER OBJECT
# WE CAN PASS FUNCTIONS AS AN ARGUMENT TO ANOTHER FUNCTION
# WE CAN RETURN FUNCTION
# WE CAN ASSIGN FUNCTION TO VARIABLES
def outer_func():
    message = 'Hi'

    def inner_func():
        print(message)

    # return inner_func()
    # This syntax will return function without executing
    return inner_func


my_func = outer_func()
# print the name of the function
# print(my_func.__name__)

# It will print the message
my_func()


# A closure is an inner function that remembers and has access
# to variables and the local scope in which it was created


def outer_func(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func


hi_func = outer_func('Hi')
hello_func = outer_func('Hello')

hi_func()
hello_func()


def outer_func(outer_msg):
    def inner_func(inner_msg):
        return f'\'outer argument : \'{outer_msg} \'inner func\'{inner_msg}'

    return inner_func


my_func = outer_func('Hi')

print(my_func('Aridon'))
