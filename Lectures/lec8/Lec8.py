import datetime

class IntSet(object):
    """
    An IntSet is set of integers
    Each int in the set occurs in self.vals exactly once.
    """

    def __init__(self):
        """
        Create empty set of integers
        """
        self.vals = []

    def insert(self, e):
        """
        Insert e into the set
        :param e: integer
        :return:
        """
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """
        :param e: integer
        :return: True if e in set and False otherwise.
        """
        return e in self.vals

    def remove(self, e):
        """
        If e in the set remove, and raise except otherwise
        :param e: integer
        :return:
        """
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found!')

    def get_member(self):
        """
        :return: list of elements
        """
        return self.vals[:]

    def __str__(self):
        """
        Returns a string representation of self
        :return:
        """
        self.vals.sort()
        result = ''
        for e in self.vals:
            result += str(e) + ', '
        return '{' + result[:-2] + '}'

"""
s = IntSet()
e = 3
s.insert(e)
s.insert(4)
print(s.member(4))
print(s.get_member())
print(s.__str__())
print(IntSet.__str__)



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

me = Person('Quan')
lover = Person('Linh')
print(me.get_name())
me.set_birthday(datetime.date(1994, 6, 23))
lover.set_birthday(datetime.date(1996, 1, 20))
print(lover.get_name() + ' is ', lover.get_age() // 356 , ' years old!')

tao = 1
print("Check instance: ", isinstance(tao, Person))

print()
person_list = [me, lover]
for p in person_list:
    print(p)
print()
person_list.sort()
for p in person_list:
    print(p)
    
"""


class Fraction(object):

    def __init__(self, num, den):
        """
        Initiation Fraction num/den
        :param num: integer
        :param den: integer
        """
        assert type(num) == int and type(den) == int
        self.num = num
        self.den = den

    def __add__(self, other):
        """
        Overwrite addition two Fractions
        :param other: Fraction
        :return: sum of two fractions
        """
        top = self.num * other.den + other.num * self.den
        bott = self.den * other.den
        return Fraction(top, bott)

    def __sub__(self, other):
        """
        :param other: Fraction
        :return: subtract of two fractions
        """
        top = self.num * other.den - other.num * self.den
        bott = self.den * other.den
        return Fraction(top, bott)

    def __float__(self):
        """
        :return: float value of a fraction
        """
        return self.den / self.num

    def inverse(self):
        return Fraction(self.den, self.num)

    def __str__(self):
        """
        printing out fraction number in string type
        :return:
        """
        return str(self.num) + '/' + str(self.den)

f1 = Fraction(3, 2)
f2 = Fraction(1, 7)

print(f1.inverse())
print(f1 - f2)
print(f1 + f2)






