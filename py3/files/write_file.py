# if the file does not exist it will create it
# if the file exist it will overwrite it
with open('file1.txt', 'w') as f:
    f.write('First Content')
    # f.seek(0) get back to the beginning of the file
    f.seek(0)
    f.write('First Content')

with open('file1.txt', 'r') as f:
    print(f.read())

# Let's have an example
# Test is in the file already written
# But if we use seek(0) method and write in the file
# a shorter content, it will overwrite only the chars
# from 0 to max length of chars
# File Content: Test
# code: f.write('R')
# File Content: Rest


with open('file1.txt', 'w') as f:
    f.write('Test')
    f.seek(0)
    f.write('R')

file = open('file1.txt', 'r')
print(file.read())
file.close()

# Example
# Copy the file to a different file

with open('file.txt', 'r') as file:
    with open('copy_file.txt', 'w') as copy_file:
        for line in file:
            copy_file.write(line)

new_file = open("copy_file.txt", "r")
 
print(new_file.read())
