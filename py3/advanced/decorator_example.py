# Practical Example #1 - Logging

def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open('logfile.txt', 'w') as file:
            fname = function.__name__
            file.write(f'{fname} returned value {value}')
            print(f'{fname} returned value {value}')
        return value

    return wrapper


@logged
def add(x, y):
    return x + y


print(add(1, 2))


