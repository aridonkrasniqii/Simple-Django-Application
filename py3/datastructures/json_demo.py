import json

with open('states.json', 'r') as file:
    data = json.load(file)

for state in data:
    print(data.get(state), end='')

for state in data['states']:
    print(state)

# print name
for state in data['states']:
    print(state.get('name'), state['abbreviation'])

# remove a key from this python file and add data to another json file

for state in data['states']:
    del state['area_codes']

with open('new_states.json', 'w') as new_file:
    # json.dump() dump the data into a file or an object
    json.dump(data, new_file, indent=4)

with open('new_states.json', 'r+') as new_file:
    new_data = json.load(new_file)

for state in new_data['states']:
    print(state)
