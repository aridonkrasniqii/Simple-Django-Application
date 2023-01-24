# Dictionary is design to store multiple key and values
# Cases when you want to describe something that has multiple attributes


person = {"name": "Jim", "age": 25}

print(person['name'])

# get dict keys with dict.keys() method
key_list = list(person.keys())
print(key_list)

# get dict values with dict.values() method
print(list(person.values()))

# get both [key & values] from the dict with dict.items() method
print(person.items())

# print key and value with for loop
for key, value in person.items():
    print(f"Key = {key} is attached to value : {value} ")

# get method - if you don't the key it will not throw an error
# ---------- it will print a default value

print(person.get('name', 'Arid'))

# update the dict with another dictionary
more_info = {"is_male": True}
person.update(more_info)
print(person)
person.clear()
print(person)