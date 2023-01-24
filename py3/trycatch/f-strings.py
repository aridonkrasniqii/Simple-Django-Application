first_name = 'Corey'
last_name = 'Schafer'

person = {'name': 'Jenn', 'age': 23}

for i in range(1, 11):
    print(f'The value is {i}')

names = ['arid', 'arid', 'arid', 'arid', 'arid']

with open('new_file.txt' , 'w') as new_file:
    for name in names:
        new_file.write(name + "\n")



