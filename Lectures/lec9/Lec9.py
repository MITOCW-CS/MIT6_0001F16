import datetime


class Person(object):

    def __init__(self, name):
        self.name = name
        self.birthday = None

    def get_name(self):
        return self.name

    def set_birthday(self, birthdate):
        self.birthday = birthdate

    def get_age(self):
        if self.birthday is None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        return self.birthday > other.birthday

    def __str__(self):
        return self.name


class MITPerson(Person):
    nextIdNum = 0

    def __init__(self, name):
        Person.__init__(name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def get_id_number(self):
        return self.nextIdNum

    def __lt__(self, other):
        return self.idNum < other.idNum
