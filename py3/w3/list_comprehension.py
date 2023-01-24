# LIST COMPREHENSION


""" Looping Using List Comprehension """
print("Looping using list comprehension ")
this_list = ['apple', 'banana', 'cherry', 'peach']
[print(x) for x in this_list]

# List comprehension offers a shorter syntax when you want to creat a new list based on
# the values of an existing list.

# Without comprehension you need to write a for statement


fruits = ['apple', 'banana', 'carry', 'kiwi', 'mango']
new_list = []

for x in fruits:
    if "a" in x:
        new_list.append(x)

print(new_list)

# With comprehension

new_list = [x for x in fruits if "a" in x]
print(new_list)

# Comprehension syntax
# new_list = [expression for item in iterable if condition == True]

# Condition - the condition is like a filter that only accepts the items that valuate to True
new_list = [x for x in fruits if x != "apple"]
print(new_list)

# With no if statement:
new_list = [x for x in fruits]
print(new_list)

# Iterable can be any iterable object, like a list, tuple, set etc.
new_list = [x for x in range(10)]
print(new_list)

#
#
# Accept only numbers lower than 5
new_list = [x for x in range(10) if x > 4]
print(new_list)

# With for loop
new_list.clear()
for x in range(10):
    if x > 4:
        new_list.append(x)
print(new_list)

#
#
#
# Expression is the current item in the iteration, but it also the outcome,
# which you can manipulate before it ends up like a list item in the new list


# Set the values to upper case
new_list = [x.upper() for x in fruits]
print(new_list)

# Set all values in the new list to 'hello'
new_list = ['hello' for x in fruits]
print(new_list)

# Return "orange" instead of "banana"
new_list = [x if x != "banana" else "orange" for x in fruits]
print(new_list)

# Return lemon instead of apple
new_list = [x if x != "apple" else "lemon" for x in fruits]
print(new_list)

# Sort list
fruits.sort()
print(fruits)

# Sort reverse
fruits.sort(reverse=True)
print(fruits)


# Customize sort function
# You can also customize your own function by using the keyword argument key = function

def my_func(n):
    return abs(n - 50)


# sort the list based on how close the numbers is to 50
the_list = [100, 50, 65, 82, 23]
the_list.sort(key=my_func)
print(the_list)

# case nsensitive sort
fruits = ["banana", "Orange", "Kiwi", "cherry"]
fruits.sort()
print(fruits)

# case insensitive sort
fruits.sort(key=str.lower)
print(fruits)

# the reverse() method reverses the current sorting order of the elements

fruits.reverse()
print(fruits)

"""
    Copy a List
    You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, 
    and changes made in list1 will automatically also be made in list2.
    There are ways to make a copy, one way is to use the built-in List method copy().
    
"""

# copy the list
first = [1, 2, 3]
second = first.copy()

# copy list with list() method
first = [1, 2, 3]
second = list(first)
print(second)

# Join two lists

# There are several ways to join, or concatenate, two or more lists in Python


# With + operator
list1 = ['a', 'b', 'c']
list2 = [1, '2', 3]
list3 = list1 + list2
print(list3)

# With append method
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
for x in list1:
    list2.append(x)
print(list2)

# With extend method
list1 = ['a', 'v', 'x']
list2 = [1, 22, 22]
print(list1[0:1])
list1.extend(list2)
print(list1)

""" 
    *** LIST METHODS *** 
    append()	Adds an element at the end of the list
    clear()	    Removes all the elements from the list
    copy()	    Returns a copy of the list
    count()	    Returns the number of elements with the specified value
    extend()	Add the elements of a list (or any iterable), to the end of the current list
    index()	    Returns the index of the first element with the specified value
    insert()	Adds an element at the specified position
    pop()	    Removes the element at the specified position
    remove()	Removes the item with the specified value
    reverse()	Reverses the order of the list
    sort()	    Sorts the list
"""

""" 
    ***Tuples***
"""
# Tuples are used to store multiple items in a single variable
# A tuple is a collection which is ordered and unchangeable
# Tuples are written with round brackets


tuple_ = ('apple', 'banana', 'cherry')

print(tuple_)

# Tuple items are ordered, unchangeable, and allow duplicate values
# Ordered:
# When we say that tuples are ordered, it means that the items have e difined order, and that order will not change
# Unchangeable:
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created

# Allow duplicates
tuple_ = ('apple', 'banana', 'cherry', 'apple', 'cherry')
print(tuple_)

# Tuple length
print(len(tuple_))

# CREATE TUPLE WITH ONE ITEM
# To create a tuple with only one itme, you have to add a comma after the item,
# otherwise Python will not recognize it as a tuple

# tuple
tuple_ = ('apple',)
print(type(tuple_))
# not a tuple
tuple_ = ('apple')
print(type(tuple_))

# Create a tuple with tuple method
tuple_ = (('apple', 'banana', 'peach'))
print(type(tuple_), tuple_)

#
#
# **** Change Tuple Values


# Once a tuple is created, you cannot change its values.Tuples are unchangeable, or immutable as it also called but
# there is a word around. You can convert the tuple into a list, change the list, and convert the list back into a tuple

# Example

x = ('apple', 'banana', 'cherry')
y = list(x)
y[1] = 'kiwi'
x = tuple(y)
print(x)

# Add items 1.

tuple_ = ('apple', 'banana', 'kiwi')
list_ = list(tuple_)
list_.append('orange')
tuple_ = tuple(list_)
print(tuple_)

# Add items 2.
# You can add a tuple to a tuple
tuple_ = ('apple', 'banana', 'carry')
y = ('orange',)
tuple_ += y
print(tuple_)

# Remove items
tuple_ = ['apple', 'banana', 'cherry']
list_ = list(tuple_)
list_.pop()
tuple_ = tuple(list_)
print(tuple_)

# Delete the entire tuple
tuple_ = ('apple', 'cherry')
del tuple_

# Unpacking a tuple
tuple_ = ('phone', 'laptop', 'ipad')
x, y, z = tuple_
print(x, y, z)

# Using asterisk *
# If the numbers of variables is less than the numbers of values, you can add an *
# to the variable name and the values will be assigned to variable as a list
tuple_ = ('phone', 'laptop', 'ipad', 'pc', 'tv')
x, y, *z = tuple_
print(x)  # first element
print(y)  # second element
print(z)  # all elements after second as a list

# Asterisk *
x, *list_, z = tuple_
print(x)
print(*list_)
print(z)  # last element

# LOOPING THROUGH THE TUPLE
print('With for loop: ')
for x in tuple_:
    print(x)

print('With range: ')
for x in range(len(tuple_)):
    print(tuple_[x])

print('With while loop')
i = 0
while i < len(tuple_):
    print(tuple_[i])
    i += 1

# Join two tuples
tuple1 = ('a', 'b', 'c')
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply tuples
# Will duplicate items in the tuple
tuple1 = ('apple', 'banana', 'cherry')
tuple1 = tuple1 * 2
print(tuple1)

# TODO:
# PYTHON SETS
