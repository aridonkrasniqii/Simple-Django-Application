# DICTIONARIES

customers = {'Name': 'Aridon',
             'Email': 'aridonkransiqi@outlook.com',
             'isVerified': True,
             'Phone': '049868210'}

# print the value of dictionary
# if the key doesn't exist an exception will be thrown
print(customers['Name'])

# print the value with get method
# if the key does not exist .get method return None
print(customers.get('name'))

# dictionary.get('key', 'default value')
print(customers.get('age', 19))

# update value
customers['Name'] = 'Arid'
print(customers.get('Name'))

# add new key
customers['Surname'] = 'Krasniqi'
print(customers.get('Surname'))

# example
numbers = {
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five'
}

number = input('Phone ')
for i in number:
    print(numbers.get(int(i)))

message = input(">")
words = message.split(" ")

emojis = {":)": "Smile ", ":(": "Cry"}

output = ""
for word in words:
    output += emojis.get(word, word)


print(word)