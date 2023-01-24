import random

# This library shouldn't be used for security purposes
# But for other things this is a great library
value = random.random()
# Each time we print this it will print a number between 0 and 1
print(value)

# If we want a random floating number in a range we can use uniform() method
value = random.uniform(1, 10)
print(value)

# Random int generator
# randint(x, y) this includes x and y
value = random.randint(1, 6)
print(value)

# 😃 If we pretend that 0 is heads and 1 is tails
value = random.randint(0, 1)
print(value)

# Let's have and example with a list to print a random element
greetings = ['Hello', 'Hi', 'Hey', 'Howdy', 'Hola']
value = random.choice(greetings)
print(value + ", arid !")

# Example with a list of random choices
# random.choices(list, k=how many times we want to get a random value)
colors = ['red', 'green', 'white']
values = random.choices(colors, k=10)

for value in values:
    print(value + " ", end="")

# In choices method we can also specify the weight of random value

print()
colors = ['red', 'white', 'black', 'green']
# So the chance for red is 12 out of 39
randoms = random.choices(colors, weights=[12, 12, 12, 3], k=10)
print(randoms)

# Shuffle the list
deck = list(range(1, 53))
random.shuffle(deck)
print(deck)

# Get a random sample from a list
deck = list(range(1, 53))
hand = random.sample(deck, k=5)
print(hand)
