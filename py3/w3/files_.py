with open('file.txt', 'w') as file:
    file.write('Aridon Krasniqi')

f = open('file.txt', 'r')

with open("file.txt", 'r') as file:
    size_to_read = 10

    file_content = file.read(size_to_read)

    while len(file_content) > 0:
        print(file_content, end='')
        file_content = file.read(size_to_read)

# Delete the file
import os

os.remove('file.txt')

if os.path.exists('file.txt'):
    print('File exists')
else:
    print('\nFile does not exist')

if os.mkdir('files'):
    print('Dir is created')
else:
    print('Dir is not created')