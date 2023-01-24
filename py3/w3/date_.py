import datetime

x = datetime.datetime.now()

print(x)

print(x.year)

print(x.strftime('%A'))
"""
    The strftime() method 
    The datetime object has a method for formatting date objects into readable strings 
    The method is called strftime(), and takes one parameter, format , to specify the format of returned string: 
"""
x = datetime.datetime(2018, 6, 1)

print(x.year)
print(x.strftime('%B'))
