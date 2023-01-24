class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'{Person.__name__} name = \'{self.name}\'  age = \'{self.age}\''


p1 = Person('Aridon', 20)

print(p1.name, p1.age, p1)


class Person:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


def printname(self):
    print(self.fname, self.lname)


class Student(Person):

    def __init__(self, fname, lname, avg_grade):
        super().__init__(fname, lname)
        self.avg_grade = avg_grade


student = Student(fname='aridon', lname='krasniqi', avg_grade=9.2)

print(student.fname, student.lname, student.avg_grade)
