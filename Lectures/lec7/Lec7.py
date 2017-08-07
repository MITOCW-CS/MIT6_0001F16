
def is_bigger(x, y):
    """
    :param x: integer
    :param y: integer
    :return: True if x less than y and False otherwise.
    """
    return x < y

def is_prime(x):
    """
    :param x: integer
    :return: True if x is prime  and False otherwise.
    """
    if x <= 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

#print(is_prime(2))

def copy(L1, L2):
    while len(L2) > 0:
        L2.pop()
    for e in L1:
        L2.append(e)
    return L2

"""
L1 = [1, 2, 3]
L2 = [4, 5, 6]

print(is_bigger(1, 2))
# normal test
print(copy(L1, L2))
# bug test
print(copy(L1, L1))


def is_pal(x):
    temp = x[:]

    print(id(temp), "  -  ", id(x))
    temp.reverse()
    if temp == x:
        return True
    return False

x = [1, 2, 3, 1]
print("TEST PALINDROME: ", is_pal(x))
"""

def sum_digits(s):
    try:
        sum = 0
        for c in s:
            if str.isdigit(c):
                sum += int(c)
        return sum
    except ValueError:
        print("Except!")

#s = 'a2b3c'
#print(sum_digits(s))

def read_int():
    while True:
        val = input('Enter an integer: ')
        try:
            val = int(val)
            return val
        except ValueError:
            print(val, 'is not an integer')

def read_val(val_type, request_msg, error_msg):
    while True:
        val = input(request_msg + ': ')
        try:
            val = val_type(val)
            return val
        except ValueError:
            print(val, error_msg)

def assertion_equal():
    try:
        x = input('Enter int = ')
        return x
    except:
        raise ValueError('x is not int')
print(assertion_equal())
#print(read_int())
#print(read_val(float, 'Enter a float number', 'is not float number!'))


