#
#
#
#
#



def capitalize(message):
    words = message.lower().split(" ")
    capitalize = []
    for i in words:
        capitalize.append(i[0].upper() + i[1:])

    return ' '.join(capitalize)


print(capitalize("aridon krasniqi"))
try:
    age = int(input("Age: "))
    value = 2000
    risk = value / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError:
    print('Invalid value')