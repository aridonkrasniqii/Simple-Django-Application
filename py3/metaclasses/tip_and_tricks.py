# 1. Ternary operator


condition = True

if condition:
    x = 1
else:
    x = 0
print(x)

condition = False
x = 1 if condition else 0
print(x)

# 2. Adding large numbers
# You can and underscore to large numbers
# it wont affect the number
num1 = 100_000_000_000
num2 = 1_000_000_000
total = num1 + num2
print(f'{total:,}')
