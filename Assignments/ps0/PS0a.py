import math

"""
    1. Ask the user to enter number x
    2. Ask the user to enter number y
    3. Prints out number x, raised to the power y
    4. Prints out the log (base 2) of x
"""

x = int(input('Enter x = '))
y = int(input('Enter y = '))
print('x ** y = ', x ** y)
print('log(', x, ')= ', int(math.log(x, 2)))