"""
    +) OOP Demonstration in the MIT-Person Management programs

    +) MIT-Person Management OOP-Graph

                    Person
                      |
                  MITPerson
                      |
                    Student
                    __|__
                   |     |
                   UG    G
"""
import datetime


class Person(object):

    def __init__(self, name):
        """ Create a person """
        self.name = name
        try:
            lastBlank = name.rindex(' ')
            self.lastName = name[lastBlank + 1:]
        except:
            self.lastName = name
        self.birthday = None

    def getName(self):
        """ Returns self's full name """
        return self.name

    def getLastName(self):
        """ Returns self's last name """
        return self.lastName

    def setBirthday(self, birthdate):
        """ Assumes birthdate is of type datetime.date
        Set self's birthday to birthdate """
        self.birthday = birthdate

    def getAge(self):
        """ Returns self's current age in days """
        if self.birthday is None:
            raise ValueError('Error: Birthday is None Value!')
        age = datetime.date.today() - self.birthday
        return age.days // 365

    def __lt__(self, other):
        """ For comparison two persons by name order """
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        """ Returns self's name in string types"""
        return self.name

""" Test Person class implementation """
# me = Person('Quan Anh Tran')
# him = Person('Trung Tuyen Nguyen')
# her = Person('Linh Thuy Tran')
#
# print('Get him last name: ', him.getLastName())
# print('Set him birthday 1995/11/02')
# him.setBirthday(datetime.date(1995, 11, 2))
# print('Him birthday: ', him.birthday)
# print('Set her birthday 1996/01/20')
# her.setBirthday(datetime.date(1996, 1, 20))
# print('Her birthday: ', her.birthday)
# print('Her last name : ', her.getLastName())
# print(her.getName(), 'is: ', her.getAge(), 'years old.')


class MITPerson(Person):
    nextIdNum = 0 # Identification number

    def __init__(self, name):
        """ Create MIT Person """
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getNum(self):
        """ Returns idNum of Person """
        return self.idNum

    def __lt__(self, other):
        """ Overloading comparision operator """
        return self.idNum < other.idNum

    def __str__(self):
        """"""
        return str(self.idNum) + ': ' + self.name

""" Testing MITPerson class """
# p1 = MITPerson('Thuy Linh')
# print(p1, 'numID: ', p1.idNum)
# p2 = MITPerson('Anh Quan')
# print(p2, 'numID: ', p2.idNum)
# p3 = MITPerson('Hai Anh')
# print(p3, 'numID: ', p3.idNum)
#
# MITPersonList = [p3, p1, p2]
# print('p1 > p2 ?: ', p1 > p2)
#
# '+ Original list: '
# for p in MITPersonList:
#     print(p, end=' | ')
#
# print()
# '+ Sorted list: '
# MITPersonList.sort()
# for p in MITPersonList:
#     print(p, end=' | ')


class Student(MITPerson):
    pass


class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year
    pass


class G(Student):

    pass



