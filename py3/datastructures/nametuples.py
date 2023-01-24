from collections import namedtuple

# It works just like a tuple but is more readable
color = (55, 155, 255)
print(color[0])

# dict
color = {'red': 55, 'green': 155, 'blue': 255}
print(color['red'])

# namedtuple
Color = namedtuple('Color', ['red', 'green', 'blue'])
color = Color(blue=55, green=155, red=255)

# specific color
white = Color(255, 255, 255)
# print special color
print(white.red)

black = Color(0, 0, 0)
print(black.red)

