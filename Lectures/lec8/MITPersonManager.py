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
    pass


class MITPerson(Person):
    pass


class Student(MITPerson):
    pass


class UG(Student):
    pass


class G(Student):
    pass



