import os

# point to current dir
# it will save all file names in a list
files = os.listdir(os.curdir)

for single_file in files:

    if single_file.endswith('.txt') or str(single_file[-4:-1]) == '.txt':
        with open(single_file, 'r') as file:
            size_to_read = 100
            content = file.read(size_to_read)

            while len(content) > 0:
                print(content)
                content = file.read(size_to_read )
