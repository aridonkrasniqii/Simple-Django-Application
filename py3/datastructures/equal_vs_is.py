# "==" checks for equality
# "is" checks for identity, if memory address is equal


l1 = [1, 2, 3, 4, 5]
l2 = l1

"""
    *** id() function *** 
    id checks for memory location
"""

print(id(l2))
print(id(l1))
print(id(l1) == id(l2))

