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
"""

