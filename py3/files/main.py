"""
f = open('alpha.txt', 'r')
# r read
# w write
# r+ read and write
# a append
# x create file if not exist
content = f.read()
print(content)
f.close()
"""

with open('alpha.txt', 'r') as file:
    content = file.read()
    print(file.mode)
if file.closed:
    print('File is closed')
else:
    print(content)

print(file.name)
print(len(content))

with open('alpha.txt', 'r') as file:
    content = file.readlines()
    for line in content:
        print(line, end='')

with open('alpha.txt', 'r') as file:
    content = file.readline()
    print(content)
    while len(content) > 0:
        content = file.readline()
        print(content)


with open('alpha.txt' , 'r') as file:
    content = file.read(100)
    while len(content) > 0:
        print(content)
        content = file.read(100)