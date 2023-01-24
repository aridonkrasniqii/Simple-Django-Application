# it has to inheritance from type to be a metaclass
class Meta(type):

    def __new__(cls, class_name, bases, attrs):
        print(attrs)
        a = {}
        for name, value in attrs.items():
            if name.startswith("__"):
                a[name] = value
            else:
                a[name.upper()] = value

        print(a)
        return type(class_name, bases, a)

class Dog(metaclass=Meta):
    x = 5
    y = 8

    def hello(self):
        print("Hi")


d = Dog()
print(d.X)