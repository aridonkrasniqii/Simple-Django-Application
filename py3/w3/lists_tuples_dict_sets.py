my_list = ['phone', 'laptop', 'ipad']
print(type(my_list))

my_list = list(('phone', 'laptop', 'ipad'))
print(type(my_list))

# List is a collection which is ordered and changeable. Allows duplicate members
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members
# Set is a collection which is unordered, unchangeable*, and un indexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members


my_list = ['laptop', 'phone', 'ipad', 'pc']
print(my_list[2:5])

if 'laptop' in my_list:
    print('Yes, laptop is in the list')

# change the second item
item = [1, 2, 3, 'Arid']
item[1] = 1
print(item)

# change two values at the same time
my_list = ['laptop', 'ipod', 'ipad', 'xbox', 'playstation']

my_list[2:4] = ['basketball', 'football']
print(my_list)

# change the second and third value by replacing it with one value:
the_list = ['apple', 'banana', 'cherry']
the_list[1:3] = ['water lemon']
print(the_list)

# if you put a str in place of brackets it will put all chars as elements in list
name_list = []
name_list[:] = 'arid'
print(name_list)

# insert method , insert(index, element)

the_list = ['apple', 'cherry', 'banana']
the_list.insert(1, 'water lemon')
print(the_list)

# insert at the end of the list
the_list[-1:] = ['peach']

# append method

thelist = ['apple', 'banana', 'cherry']
thelist.append('orange')
print(thelist)

# Extend list
# To append elements from another list to current list, use extend()
first = ['apple', 'banana', 'cherry']
second = ['mango', 'pineapple', 'papaya']
first.extend(second)
print(first)

# Remove specific item
items = ['apple', 'banana', 'cherry']
items.remove('apple')
print(items)

# Remove specific index with pop function
items = ['apple', 'cherry', 'banana']
items.pop(items.index('cherry'))
print(items)

# The del keyword also removes the specific index:
items = ['apple', 'banana', 'cherry']
del items[0]
print(items)

# Delete entire list
items = ['apple', 'banana']
del items

# Clear the list content
items = ['apple', 'banana', 'cherry']
items.clear()
print(items)

# Loop through the list


items = ['apple', 'banana', 'cherry']

for x in items:
    print(x)

for x in range(len(items)):
    print(items[x])

i = 0
while i < len(items):
    print(items[i])
    i += 1
