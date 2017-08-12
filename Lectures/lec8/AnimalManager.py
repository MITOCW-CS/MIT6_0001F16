"""
Animal manager

                  Animal
              ______|______
             |      |      |
           Rabbit  Cat   Person
                           |
                        Student

1. Animal
    - Attributes:
        + age
        + name
    - Methods:
        + init(age)
        + get_age()
        + get_name()
        + set_age(new_age)
        + set_name(new_name)
        + str()
2. Cat
    - Attributes:
        None
    - Methods:
        + speak()
        + str()
3. Person
    - Attributes:
        + name
        + age
        + friends[]
    - Methods:
        + get_friends()
        + speak()
        + add_friends()
        + age_diff()
        + str()
4. Student
    - Attributes:
        + name
        + age
        + major
    - Methods:
        + str()
        + change_major()
        + speak()
5. Rabbit
    - Attributes:

"""


class Animal(object):

    def __init__(self, age):
        """ Create Animal Object """
        self.age = age
        self.name = None

    def get_age(self):
        """
        :return: self's age
        """
        return self.age

    def get_name(self):
        """
        :return: self's name
        """
        return self.name

    def set_age(self, new_age):
        """
        :param new_age: name
        :return: set self's age to new age
        """
        self.age = new_age

    def set_name(self, new_name):
        """
        :param new_name: string
        :return: set self's name to new name
        """
        self.name = new_name

    def __str__(self):
        """
        :return: string object of Animal instances
        """
        return "+ animal: " + str(self.name) + " -- age: " + str(self.age)


""" Testing Animal Class """

# animal = Animal(12)
# animal.set_name('Dog')
# animal.set_name('sssssss')
# animal.set_age(1222)
# print(animal)


class Cat(Animal):
    def __init__(self, color, age):
        Animal.__init__(self, age)
        self.color = color

    def speak(self):
        print("meow")

    def __str__(self):
        return "cat: " + str(self.name) + ' -- color: ' + self.color + ' -- age: ' + str(self.age)

""" Testing Cat Class """

# cat = Cat('RED', 22)
# cat.speak()
# cat.set_name('Tom')
# print('get age: ', cat.get_age())
# print('get name: ', cat.get_name())
# cat.set_name('Jerry')
# print(cat)


class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = []

    def get_friends(self):
        return self.friends

    def speak(self):
        print('Hello')

    def add_friends(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)

    def age_diff(self, other):
        diff = abs(self.age - other.age)
        print('Ages diff = ', diff)

    def __str__(self):
        return 'Person: ' + str(self.name) + ' | Age: ' + str(self.age)


""" Testing Person Class """

p1 = Person('Thuy Linh', 21)
p2 = Person('Anh Quan', 23)
a = Animal('22')
p1.age_diff(p2)
print(p1.get_age())
p1.add_friends(p2)
p1.add_friends(a)

print('Friend: ')
for friend in p1.friends:
    print(friend)
print()
print(p1)
print(p2)