class Employee:

    def __init__(self, id: int, name: str, faculty: str):
        assert id >= 0, 'Id should be more than zero'
        assert len(name) >= 0, 'Name should not be empty'
        self.id = id
        self.name = name
        self.faculty = faculty

    def print_details(self):
        return '{} {} {}'.format(self.id, self.name, self.faculty)


class Developer(Employee):
    skills = []

    def __init__(self, id, name, faculty):
        super().__init__(
            id, name, faculty
        )

    def add_skill(self, skill):
        if skill not in self.skills:
            LogFile.log_file(f'Skill {skill.name} is added')
            self.skills.append(skill)
        else:
            return False

    def remove_skill(self, skill):
        if skill not in self.skills:
            print('Skill is not in the list')
        else:
            LogFile.log_file(f'Skill {skill.name} is removed')
            self.skills.remove(skill)

    def most_rated(self):
        max_rate = self.skills[0].rate
        for skill in self.skills:
            if skill.rate > max_rate:
                max_rate = skill.rate

        LogFile.log_file('Most rated skill is being printed')
        return max_rate

    def change_rate(self, id, new_skill):
        for skill_ in self.skills:
            if skill_.id == id:
                skill_.name = new_skill

                LogFile.log_file(f'Skill {skill_.name}is changed ')


class Skill:

    def __init__(self, id: int, name: str, rate):
        self.__id = id
        self.__name = name
        self.__rate = rate

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def rate(self):
        return self.__rate

    @id.setter
    def id(self, id):
        self.__id = id

    @name.setter
    def name(self, name):
        self.__name = name

    @rate.setter
    def rate(self, rate):
        self.__rate = rate


class LogFile:
    @staticmethod
    def log_file(message):
        with open('log_file.txt', 'a') as file:
            file.write(message + "\n")


developer = Developer(id=1, name='Arid', faculty='fiek')
skill1 = Skill(id=1, name='Python Coming Soon...', rate=3)
skill2 = Skill(id=2, name='Java', rate=10)

developer.add_skill(skill1)
developer.add_skill(skill2)
developer.remove_skill(skill1)
print(developer.most_rated())
developer.change_rate(2, 'Java again, haha ')

for skill in developer.skills:
    print(skill.name)