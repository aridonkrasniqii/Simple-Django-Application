my_list = [0, 1, 2, 3, 4, 5, 6, 7]
# list [start:end:step]

print(my_list[3:8])

# 1 to the end
print(my_list[1:])

# 0 to -1
print(my_list[:-1])

# step allows you to skip a certain number of values
# if step = 2 =>  i = i + 2
print(my_list[2:-1:2])

# negative step
print(my_list[-1:2:-1])

# reverse the array
print(my_list[::-1])

# print from 6 to 2
print(my_list[-2:1:-1])

# Slicing strings

# slice a sample url

sample_url = 'http://coreyms.com'

print(sample_url)

# print in reverse
print(sample_url[::-1])

# get the top level domain from this url
print(sample_url[sample_url.index('.') + 1:])
# or hard coded
print(sample_url[-3:])

# print the url without http://
print(sample_url[7:])