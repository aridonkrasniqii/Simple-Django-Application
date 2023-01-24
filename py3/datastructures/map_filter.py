# def square(a):
# return a * a
# result_of_five = square(5)
# print(result_of_five)


square = lambda x: x ** 2
print(square(10))

multiply = lambda x, y: x * y
print(multiply(1, 2))


def even_numbers(list_of_numbers):
    even = []
    for i in list_of_numbers:
        if not (i % 2):
            even.append(i)
    return even


print(even_numbers(range(1, 10)))


def even_numbers(list_of_numbers):
    for i in list_of_numbers:
        if i % 2 == 0:
            yield i


list_ = list(even_numbers(range(1, 10)))
print(list_)


def even_number(number):
    if number % 2 == 0:
        return number


event_digits = map(even_number, range(1, 10))
# event_digits  = [x for x in event_digits if x != None]
print(event_digits)
# function filter(Element to filter , data type)
event_digits_filtered = filter(None, event_digits)
print(list(event_digits_filtered))

from employees import employees

