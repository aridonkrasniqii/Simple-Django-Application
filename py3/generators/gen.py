# gen.py


from time import sleep
import mysql.connector


def add1(x,  y):
    return x + y


class Adder():
    def __call__(self, x, y):
        return x + y


add2 = Adder()


def compute():

    rows = []

    for _ in range(10):
        sleep(.5)
        rows.append(_)

    return rows


class Compute():

    # def __call__(self):

    #     rv = []
    #     for _ in range(10):
    #         sleep(5)
    #         rv.append(_)

    #     return rv

    def __iter__(self):
        self.last = 0
        return self

    def __next__(self):
        rv = self.last
        self.last += 1
        if self.last > 10:
            raise StopIteration
        sleep(.5)
        return rv


def compute():

    for i in range(10):
        sleep(.5)
        yield(i)


for val in Compute():
    print(val)
