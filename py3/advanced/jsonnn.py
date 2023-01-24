import json as json

json_str = """{
  "squadName": "Super hero squad",
  "homeTown": "Metro City",
  "formed": 2016,
  "secretBase": "Super tower",
  "active": true,
  "members": [
    {
      "name": "Molecule Man",
      "age": 29,
      "secretIdentity": "Dan Jukes",
      "powers": [
        "Radiation resistance",
        "Turning tiny",
        "Radiation blast"
      ]
    },
    {
      "name": "Madame Uppercut",
      "age": 39,
      "secretIdentity": "Jane Wilson",
      "powers": [
        "Million tonne punch",
        "Damage resistance",
        "Superhuman reflexes"
      ]
    },
    {
      "name": "Eternal Flame",
      "age": 1000000,
      "secretIdentity": "Unknown",
      "powers": [
        "Immortality",
        "Heat Immunity",
        "Inferno",
        "Teleportation",
        "Interdimensional travel"
      ]
    }
  ]
}
"""


json_data = json.loads(json_str)


print(isinstance(json_data, dict))
print("SquadName= '" + str(json_data['squadName']) + "'")
print("HomeTown= '" + str(json_data.get('homeTown') + "'"))
print("***** Members **** ")
for member in json_data['members']:
    print(member)
print("**** Members **** ")

for member in json_data['members']:
    print("{")
    for key, value in member.items():
        print(f'\t"{key}": "{value}"')
    print("}")


# lets delete secret identity

for member in json_data['members']:
    del member['secretIdentity']


new_json_string = json.dumps(json_data, indent=2)
print(new_json_string)

print()

for member in json.loads(new_json_string)['members']:
    print(member)


# let's work with some files now


with open('application.json') as json_file:
    json_from_file = json.load(json_file)

print(isinstance(json_from_file, dict))


for member in json_from_file['members']:
    del member['age']


with open('new_application.json', 'w') as new_file:
    json.dump(json_from_file, new_file, indent=2)


