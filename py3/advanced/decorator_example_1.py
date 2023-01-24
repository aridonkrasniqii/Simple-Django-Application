# Practical Example #2: Timing
import time


def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        returned_value = function(*args, **kwargs)
        after = time.time()
        function_name = function.__name__
        print(f'{function_name} took {after - before} seconds to execute')

        return returned_value

    return wrapper


@timed
def myfunction(x):
    result = 1
    for i in range(1, x):
        result *= i

    return result

print(myfunction(10000))