import itertools

# counter = itertools.count()

"""for num in counter:
    print(num)
"""
# data = [100, 200, 300, 400]

# daily_data = list(zip(itertools.count(), data))
# print(daily_data)


"""print(next(counter))
print(next(counter))
print(next(counter))"""

#
# counter = itertools.count(start=5, step=2)
# print(next(counter))
# print(next(counter))
# print(next(counter))


data = [100, 200, 300, 400]
daily_data = list(zip(itertools.count(), data))


print(daily_data)


daily_data = list(zip(range(10), data))
print(daily_data)


daily_data = list(itertools.zip_longest(range(10), data))
print(daily_data)


daily_data = itertools.cycle([1,2,3])
# cikel


print(next(daily_data))
print(next(daily_data))
print(next(daily_data))
print(next(daily_data))
