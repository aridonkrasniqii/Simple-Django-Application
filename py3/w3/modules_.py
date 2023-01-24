from mymodule import greeting

greeting('Aridon')
"""
    import mymodule 
    mymodule.greeting('Aridon')
"""

from mymodule import person

a = person
name = person.get('name')
print(a)

for key in person.keys():
    print(person.get(key))

#  Re-naming a module
# import mymodule as mx
