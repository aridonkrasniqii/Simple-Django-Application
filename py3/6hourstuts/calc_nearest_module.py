
while True:
    number = int(input("Write the number "))
    if not number % 3:
        print(f'Number {number} is module 3')
        continue

    theNumber = round(number / 3)
    theNumber = theNumber * 3
    print(f'Number near {number} is {theNumber} which is module 3')
