my_tuple = ('apple', 'banana', 'cherry')
myit = iter(my_tuple)

"""
    An iterator is ana object that contains a countable number of values.
    An iterator is an object that can be iterated upon, meaning that you can traverse through all the values 
    
"""
print(next(myit))

""" 
    Iterator vs iterable
    
    Lists, tuples, dictionaries and sets are all iterable objects 
    They are iterable containers which you can get an interator from 
    All these objects have a iter() method which is used to get an  iterator: 
    
"""

my_tuple = ('apple', 'banana', 'cherry')

myit = iter(my_tuple)
print(next(myit))
print(next(myit))
print(next(myit))

# Strings are also iterable objects, containing a sequence of characters:

mystr = 'banana'
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Looping through an iterator

my_tuple = ('apple', 'banana', 'cherry')

for x in my_tuple:
    print(x)
