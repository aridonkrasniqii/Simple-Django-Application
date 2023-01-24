""" All methods to create classes """


# Method 1
class A(object):

    def __init__(self):
        pass


# Method 2
class B(object):

    def __new__(cls, *args, **kwargs):
        return super(B, cls).__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        super(B, self).__init__(*args, **kwargs)


# Method 3
class C(object):

    def __call__(cls, *args, **kwargs):
        return super(C, cls).__call__(cls)


# Method 4


class D(type):

    def __call__(cls, *args, **kwargs):
        instance = super(D, cls).__call__(*args, **kwargs)
        return instance

    def __init__(cls, name, base, attr):
        super(D, cls).__init__(name, base, attr)


class E(metaclasses=D):

    def __init__(self, *args, **kwargs):
        pass
