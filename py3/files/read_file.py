# File object

# We can read the file
# We can write the file
# We can append the file
# We can read and write the file

f = open('file.txt', 'r')
# Print the name of the file
print(f.name)
# Close the file
# If we don't close the file then you can
# end up leaks that cause you to run over the maximum allowed
# file descriptors on your system and application could throw an error
f.close()
# Mode of the file r, w, a, r+
print(f.mode)

# with will automatically close the file
with open('file.txt', 'r') as f:
    pass
# we have access to the file after with scope
# but the file will be closed
print(f.closed)

# If we have a small file this is correct
with open('file.txt', 'r') as f:
    f_content = f.read()
    print(f_content)

# Read lines of a file
with open('file.txt', 'r') as f:
    f_lines = f.readlines()
    # Print one line
    f_line = f.readline()
    print(f_line)
for line in f_lines:
    print(line)

# To get rid of the new line in the list we can use end=''
with open('file.txt', 'r') as f:
    f_lines = f.readlines()

for line in f_lines:
    print(line, end='')

# Read the entire file with readline() method
with open('file.txt', 'r') as f:
    while line != '':
        line = f.readline()
        print(line, end='')

# Read the file with for loop
with open('file.txt', 'r') as f:
    for line in f:
        print(line, end='')

# Read the file with method read()
with open('file.txt', 'r') as f:
    print(f.read)

# In read() method we can specify the size of the file that we want to read

with open('file.txt', 'r') as f:
    # Will print the first 100 characters in the file
    f_content = f.read(100)
    print(f_content, end='')
    # Read the 100 hundred other chars in the file
    f_content = f.read(100)
    print(f_content, end='')

with open('file.txt', 'r') as f:
    size_to_read = 100
    file_content = f.read(size_to_read)
    # Tell in which position you are in the file
    print(f.tell())
    """***** IMPORTANT *****"""
    # The idea of using a specific size to read a file is that
    # when you have big files you cannot store them into a variable
    # So you need to read the file by parts using a size, like example shown below

    while len(file_content) > 0:
        print(file_content)
        file_content = f.read(size_to_read)

print()
# f.seek(position of the file )
with open('file.txt', 'r') as f:
    size_to_read = 0

    f_content = f.read(size_to_read)
    print(f_content, end='')
    f.seek(0)

    f_content = f.read(size_to_read)
    print(f_content, end='')




