"""
    To create an object/class as an iterator you have to implement the methods __iter__()
    and __next()__  to your object

    The __iter__() , you can do operations (initialzing etc) but must always return the iterator object itself
    The __next__() , method also allows you to do operations, and must return  the next item in the sequence

"""


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


my_class = MyNumbers()
myiter = iter(my_class)

print(next(myiter))
print(next(myiter))
print(next(myiter))


# StopIteration

# To prevent the iteration to go on forever, we can use the StopIteration statement In the __next()__ method,
# we can add a terminating condition to raise an error if the iteration is done a specified number of times
class MyNumbers:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


my_class = MyNumbers()
myiter = iter(my_class)

for x in myiter:
    print(x)

x = 300


def my_func():
    global x
    x = 200


my_func()
print(x)