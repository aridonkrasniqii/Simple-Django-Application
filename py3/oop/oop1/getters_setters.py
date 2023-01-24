class Employee:

    def __init__(self, first, last):
        self.__first = first
        self.__last = last
        self.email = first + ' ' + last + '@email.com'

    def fullname(self):
        return '{} {}'.format(self.__first, self.__last)

    @property
    def first(self):
        return self.__first

    @property
    def last(self):
        return self.__last

    @first.setter
    def first(self, first):
        self.__first = first

    @last.setter
    def last(self, last):
        self.__last = last

    @first.deleter
    def first(self):
        self.first = None


emp = Employee('Arid', 'Krasniqi')
emp.first = emp.first.lower()

print(emp.first)

del emp.first

try:
    if emp.first is None:
        raise Exception()
    print(emp.first)
except Exception:
    print('First is deleted')
