"""
# exhaustive enumeration
x = float(input("x = "))
ESP = 0.01
step = ESP ** 3
numGuesses = 0
ans = 0.0

while abs(ans ** 2 - x) >= ESP and ans * ans <= x:
    ans += step
    numGuesses += 1

print("numGuesses = ", numGuesses)
if abs(ans ** 2 - x) >= ESP:
    print("Failed on root x = ", x)
else:
    print("ans = ", ans, "x = ", x)
"""

"""
# bisection search
x = int(input("x = "))
ESP = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (low + high) / 2.0

while abs(ans ** 2 - x) > ESP:
    # print("low = ", low, ",high = ", high, ",ans = ", ans)

    numGuesses += 1
    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (low + high) / 2.0

print("root of x = ", x, " is ", ans)
print("numGuesses = ", numGuesses)
"""

"""
# Newton-Raphson for square root
# Find x such that x^2 - 24 = 0 within epsilon = 0.01

ESP = 0.01
k = float(input("k = "))
numG = 0
guess = k/2.0
while abs(guess * guess - k) >= ESP:
    numG += 1
    guess = guess - (guess * guess - k) / (2 * guess)
print("guess = ", numG)
print("square root of ", k, "is", guess)
"""

"""
# play with string

s = "hello"
# s[0] = 'y' # make error string immutable

s = 'y' + s[0:len(s)]
#print(s)

s = 'abcdefgf'
# print out substring of s from index 3 to index 6 with default step equal to 1
print(s[3:6])
# print print out substring of s from index 3 to index 6 with default step equal to 2
print(s[3:6:2])
# print entire string s equivalent s[0:len(s)]
print(s[::])
# print out s in reverse order
print(s[::-1])
"""

def exhaustive_enumeration(x, esp):
    """
    Find root by exhaustive enumeration method
    :param x: a integer number
    :param esp: epsilon
    :return: number y such that y ^ 2 = x
    """

    step = esp ** 2
    num_guesses = 0
    ans = 0.0

    while abs(ans ** 2 - x) >= esp and ans * ans <= x:
        ans += step
        if num_guesses > 10000:
            print("NUM GUESSES > 10000")
            break
        num_guesses += 1

    if abs(ans ** 2 - x) > esp:
        print("Failed on find root x = ", x)
        return
    else:
        return ans, num_guesses


def bisection(x, esp):
    """
    Find root by bisection method
    :param x:
    :param esp:
    :return:
    """

    num_guesses = 0
    low = 0.0
    high = max(1.0, x)
    ans = (low + high) / 2.0
    while abs(ans ** 2 - x) > esp:
        num_guesses += 1
        if ans ** 2 > x:
            high = ans
        else:
            low = ans
        ans = (low + high) / 2.0
    return ans, num_guesses

def Newton_Raphson(x, esp):
    num_guesses = 0
    guess = x / 2.0

    while abs(guess * guess - x) > esp:
        num_guesses += 1
        guess = guess - (guess * guess - x) / (2 * guess)

    return guess, num_guesses


def bisection1(x, n, esp):
    """
    Find root by bisection method
    :param x:
    :param esp:
    :param n:
    :return:
    """

    num_guesses = 0
    low = 0.0
    high = max(1.0, x)
    ans = (low + high) / 2.0
    while abs(pow(ans, n) - x) > esp:
        num_guesses += 1
        if pow(ans, n) > x:
            high = ans
        else:
            low = ans
        ans = (low + high) / 2.0
    return ans, num_guesses

if __name__ == '__main__':

    x, n, esp = 625, 4, 0.01
    print("x = ", x, "Epsilon = ", esp)
    print("--------- EXHAUSTIVE ENUMERATION METHOD -----------")
    print("ans, number guesses =", exhaustive_enumeration(x, esp))
    print("-------------- BISECTION METHOD -------------------")
    print("ans, number guesses =", bisection(x, esp))
    print("-------------- NEWTON_RAPHSON METHOD --------------")
    print("ans, number guesses =", Newton_Raphson(x, esp))
