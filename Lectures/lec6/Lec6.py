# MIT6_0001F16_Lecture 6: Recursion, Dictionaries

"""
    calculate factorial of integer n
    using recursion method
"""

def factI(n):
    res = 1
    while n > 0:
        res *= n
        n -= 1
    return res

def factR(n):
    if n == 1:
        return n
    return n * factR(n - 1)


n = 5
assert (factI(n) == factR(n))
print("FI = ", factI(n), "FR = ", factR(n))

"""
    calculate fibonacci of integer n
    using recursion method
"""


def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

n = 11
print("FIB = ", fib(n))

# Tower of HaNoi problem


def print_move(fr, to):
    print("Move from", fr, "to", to)


def tower(n, fr, to, temp):
    if n == 1:
        print_move(fr, to)
    tower(n - 1, fr, temp, to)
    tower(1, fr, to, temp)
    tower(n - 1, temp, to, fr)

tower(4, 'P1', 'P2', 'P3')

"""
    check Palindrome of a string
"""


def is_palindrome(s):
    def to_char(s):
        s = s.lower()
        letter = ''
        for c in s:
            if str.isalpha(c):
                letter += c
        print(letter)
        return letter

    def is_pal(s):
        if len(s) <= 1:
            return True
        return s[0] == s[-1] and is_pal(s[1:-1])

    return is_pal(to_char(s))

s = '123'
print("s = ", s, " - PAL = ", is_palindrome(s))


"""
    Dictionary
"""

print("DICT TESTING ...")
monthNumbers = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr'}

print(monthNumbers[1])

print("\nDEBUG")
dict1 = {'hai': 2, 'ba': 3, 'bon': 4}

def search_key(k, d):
    return d.get(k, d)


k = '111'
print("Test searching: ", search_key(k, dict1))






