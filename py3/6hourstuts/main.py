# print()
# input()
# int()
# bool()
# float()
# type()
# """ Multiple line string """
# str[started_index: end_index]
# str[0:empty] [0:] entire string
# str[:5] 0 to 5
# str[:] entire string
# formatted string str = f''
# course.upper()
# course.lower()
# course.find() find char or a complete word returns the first index of letter
# course.replace()
# if it contains  \\  'Word' in variable \\ returns bool
# course.upper()
# course.lower()
# course.find()
# course.replace()
# '...' in course
# * ** / // the ceil part
# round()  round the number
# abs() convert in to positive
# math.ceil upper part
# math.floor lower part
# for letter in range(1 ,10 ,2) which means i += 2
# names = ['John', 'Bob','Mosh','Sarah']
# print(names[2:0])
# numbers = [1, 24, 7, 8, 6]
# max(numbers)
# list.append(element)
# list.insert(index, element)
# list.remove(element)
# list.clear() remove all elements in array
# list.pop() append to the end
# list.index(element) returns the index of element
# element in list returns false or true
# list.count(element) number of this element in list
# list.sort() sort the list ascending
# list.reverse() sort the list descending
# list.copy() will copy the list
# and the second list will not be effected
# numbers = [1, 2, 6, 4, 5]
# numbers2 = numbers.copy()
# numbers.append(10)
# numbers.sort()
# print(numbers)


# REMOVE THE DUPLICATES IN LIST
# numbers = [1, 2, 2, 2, 3, 4, 4, 5]
#
# for i in numbers:
#     if numbers.count(i) > 1:
#         numbers.remove(i)
#
# print(numbers)
# THE SECOND FORM TO REMOVE THE  DUPLICATES IN THE LIST
# numbers = [1, 3, 4, 5, 6, 10, 10, 10]
# uniques = []
#
# for i in numbers:
#     if i not in uniques:
#         uniques.append(i)
#     else:
#         continue
# print(uniques)

# TUPLES
# TUPLES ARE SIMILAR TO LISTS
# WE CAN USE THEM TO STORE A LIST OF ITEMS
# UNLIKE LISTS WE CANNOT ADD NEW ITEMS,
# WE CANNOT REMOVE EXISTING ITEMS
# TUPLES ARE IMMUTABLE

# numbers = (1, 2, 3)
# tuple.count()
# tuple.index()
# WE ONLY CAN GET INFORMATION FROM TUPLES
# for i in numbers:
#     print(i)


# UNPACKING or DESTRUCTURING

# coordinates = (1, 2, 3)
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
# x, y, z = coordinates
#
# print(x, y, z)
