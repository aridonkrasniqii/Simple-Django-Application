my_list = [1, 2, 'Aridon']

another_list = [4, 5, 6]
# method extend will merge the list
my_list.extend(another_list)

print(my_list)

import os

# os.system('command you want to be executed to command line')
os.system('ls')

# first parameter is the index and the second is the element
my_list.insert(0, 100)
print(my_list)

# list.sort() method will sort the list ascending
new_list = [1, 2, 6, 4, 3]
new_list.sort()
print(new_list)

# list.sort(reverse=True) method will sort the list by descending
new_list.sort(reverse=True)
print(new_list)
new_list.sort()
# or we can sort it with the method reverse
new_list.reverse()
print(new_list)


stack = ["John", "Jim" ]

# append method will put the element at the end of the list
stack.append('Alien')
print(stack)
# pop method will pop the last element in the list
stack.pop()
print(stack)








