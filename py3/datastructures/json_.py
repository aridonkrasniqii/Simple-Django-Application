import json

"""
JavaScript Object Notation
"""

# json very common data format for storing information

people_string = '''
{
    "people":
    [
        {
        "name": "John Smith",
         "phone": "61231-12312-12",
         "emails": ["aridon@email.com","aridon1@email.com"]
        },
        {   
        "name":"Jane Doe",
        "phone":"6450-5445-454",
        "emails" :null
        }
    ]
}
'''

data = json.loads(people_string)
print(type(data))
print(data)
print(type(data['people']))

for people in data.get('people'):
    print(people, end=' ')
for people in data['people']:
    print(people, end=' ')

# Print name of people
print()
for people in data['people']:
    print(people['name'])

# Delete phone from people
for people in data['people']:
    del people['phone']

new_string = json.dumps(data)
# create new json data
print(new_string)

# you can set up indent to make data more readable

new_string_1 = json.dumps(new_string, indent=2, sort_keys=True)

print(new_string_1)
