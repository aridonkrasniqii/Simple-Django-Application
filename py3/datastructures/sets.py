my_set = {
    "Allen", "Jim", "John"
}
print(my_set)
# will remove the duplicate values
a_list = ["Jim", "Jim", "John"]
# convert list to set // set(list)
# convert set to list // list(set)
a_set = set(a_list)

# check if a specific element exist
print("John" in my_set)
print("Jack" in my_set)

# convert a string into a set
programming = set("Python")
print(programming)

set1 = set("abc")
set2 = {"c", "d", "e"}
# check for similarities in both sets
# what exist in both sets
print(set1.intersection(set2))

# union - will union to sets together
print(set1.union(set2))

# difference - it will return the differences
print(set1.difference(set2))

# what set2 has and set1 does not
print(set2.difference(set1))

# symmetric_difference the unique elements between two sets
print(set1.symmetric_difference(set2))




