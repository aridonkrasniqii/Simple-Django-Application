nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Copy an array
my_list = []
for n in nums:
    my_list.append(n)

# print(my_list)

# Copy array with comprehension
my_list = [n for n in nums]

# print(my_list)


my_list.clear()
# Copy n*n for each n in nums
for n in nums:
    my_list.append(n * n)
# print(my_list)

my_list = [n * n for n in nums]
# print(my_list)


my_list.clear()

# Copy the even n in nums
for n in nums:
    if n % 2 == 0:
        my_list.append(n)
# print(my_list)

# Copy the even n in nums
my_list = [n for n in nums if n % 2 == 0]
# print(my_list)

# if n % 2 is 0 not will make it 1 , so true
my_list.clear()
my_list = [n for n in nums if not n % 2]

# I want a (letter,num) pair for each letter in 'abcd' and each number in '0123'

my_list.clear()
for i in 'abcd':
    for j in range(4):
        my_list.append((i, j))
print(my_list)

# Let's make with comprehension
my_list.clear()
my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)

# Dictionary comprehensions

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Hulk', 'Deadpool']

# I want a dict {'name': 'hero'} for each name,hero

my_dict = {}
for num in range(len(names)):
    my_dict[names[num]] = heroes[num]

# print(my_dict)

my_dict.clear()
# With zip function which creates a tuple (name,hero)
for name, hero in zip(names, heroes):
    my_dict[name] = hero

# print(my_dict)


my_dict.clear()
# With comprehension
my_dict = {name: hero for name, hero in zip(names, heroes)}
print(my_dict)

# Put constraints in comprehension
# If name not equal to Peter
my_dict.clear()
my_dict = {name: hero for name, hero in zip(names, heroes) if name != 'Peter'}
print(my_dict)

# Set comprehensions

nums = [1, 1, 2, 2, 1, 3, 4, 5, 6, 6, 2, 3, 4, 2, 3, 9, 6, 7, 8, 6, 7]
# set is a list that has unique values
my_set = set()
for num in nums:
    my_set.add(num)

# print(my_set)
my_set.clear()
my_set = {num for num in nums}
print(my_set)

# Generator Expressions

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def gen_func(nums):
    for n in nums:
        yield n * n


my_gen = gen_func(nums)
for i in my_gen:
    print(i)

# type if generator
print(type(my_gen))

my_gen = ()
my_gen = (n * n for n in nums)
for i in my_gen:
    print(i)

