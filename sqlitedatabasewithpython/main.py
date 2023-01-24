numbers = [x for x in range(1, 100)]

prime_numbers = []


def check_number(number):
    for i in range(2, number):
        if (number % i) == 0:
            return False

    return True


for num in numbers:
    if check_number(num):
        prime_numbers.append(num)

print(f"Prime numbers: {prime_numbers}")