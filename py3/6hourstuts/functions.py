def greetUser(firstName='Arid', lastName='Krasniqi'):
    print(f'Hi {firstName} {lastName}')
    print('Welcome  aboard')


print("Start")
greetUser(lastName='Krasniqi')
print("Finish")


def square(number):
    return number * number


print(square(10))

print(type(None))


def convertEmoji(message):
    words = message.split(" ")

    emojis = {
        ":(": "Cry",
        ":)": "Smile"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "

    return output


print(convertEmoji(input(">")))
