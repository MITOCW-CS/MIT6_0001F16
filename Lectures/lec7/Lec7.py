
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

L1 = [1, 2, 3]
L2 = [4, 5, 6]

# normal test
print(copy(L1, L2))
# bug test
print(copy(L1, L1))