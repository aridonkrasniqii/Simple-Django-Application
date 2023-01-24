import random

"""
    Text Type:	str
    Numeric Types:	int, float, complex
    Sequence Types:	list, tuple, range
    Mapping Type:	dict
    Set Types:	set, frozenset
    Boolean Type:	bool
    Binary Types:	bytes, bytearray, memory view
    None Type:	NoneType
"""

x = "Python is gonna be my wifey"
x = 20
x = 20.5
x = 1j  # complex data type
x = ['phone', 'laptop', 'pc']
x = ('phone', 'laptop', 'pc')
x = range(6)
x = {'name': 'arid', 'age': 20}
x = {'phone', 'laptop', 'pc'}
x = frozenset({'phone', 'laptop', 'pc'})
x = True
x = b'Hello'  # bytes
x = bytearray(5)
x = memoryview(b'arid')
x = None

# Complex numbers
x = 3 + 5j
y = 5j
z = -5j
print(f'{x} numbers is a type of {x.__class__.__name__}')

# Type Conversion


x = 1
y = 1.8
z = 1j

a = float(x)
b = int(y)
c = complex(x)
print(a, b, c)

"""
    **RANDOM NUMBER**
"""

i = 0
while i <= 5:
    i += 1
    print(random.randrange(1, 10))

"""
    **Python Casting**
"""
x = int(1)
y = int(2.8)
z = float("3")

a = """
    Lorem ipsum dolor sit amet,
    consectetur adipiscing elit,
    sed do eiusmod tempor incididunt
    ut labore et dolore magna aliqua
"""

print(a)

# Looping through a string
for x in 'type()':
    print(x)

# String length
for x in range(len('string')):
    print(x)

# Check String - in
txt = "The best things in life are free!"
print("free" in txt)

if "free" in txt:
    print(txt)

# if not
if "expensive" not in txt:
    print('Expensive is not present')

# Slicing Strings

s = "Python programming language"
print(s[:])
print(s[-8:])

# lower() upper()
print(s.upper())
print(s.lower())

# Remove whitespace - strip()
s = 'Remove    whitespaces  '
print(s.strip())

# Replace replace(find, replace)
print(s.replace('Remove', 'Strip'))

#  split() returns a list  where the text between the specified separator
print(s.split(' '))

# Concat strings with +
a = "str1"
b = "str2"
print(a + b)

# format() method takes the passed arguments,formats them, and places them in the string where placeholders {} are.
age = 19
txt = 'My name is Aridon, and I am {}'
print(txt.format(age))

# format() example
quantity = 3
item_no = 567
price = 49.95
my_order = 'I want {} pieces of item {} for {} dollars '
print(my_order.format(quantity, item_no, price))

# format example
# you can use index numbers {0} to be sure the arguments are placed in the correct placeholders
quantity = 3
item_no = 400
price = 49.95
my_order = 'I want to pay {2} dollars for {0} pieces of item {1}'
print(my_order.format(quantity, item_no, price))

# BOOLEANS
print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 20
b = 5
if a > b:
    print(f'{a} is greater than {b}')
else:
    print(f'{b} is greater than {a}')

# bool
print(bool("Hello"))  # returns true
print(bool(15))  # returns true

# Any string is True, except empty strings
# Any numbers is True, except 0
# Any list, tuple, set and dict is True, except empty ones

print(bool('abc'))
print(bool(123))
print(bool(['apple', 'cherry', 'banana']))

# False values
print(bool(False))
print(bool(0))
print(bool(None))
print(bool(""))
print(bool({}))
print(bool(()))
print(bool([]))


class myClass:
    def __len__(self):
        return 0


obj = myClass()
print(bool(obj))

# Check if an object is a certain data type with isinstance() method


x = 200
print(isinstance(x, int))
x = 2.0
print(isinstance(x, float))
x = ""
print(isinstance(x, str))




