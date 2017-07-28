"""
t1 = ('two', 4)
t2 = (1, 'two', 3)
def intersect(t1, t2):
    t = ()
    for e in t1:
        for f in t2:
            if e == f:
                t += (e, )
    return t

# print(intersect(t1, t2))

a,b,c = 'xyz'
# print(a, b, c)

x = []
# print(type(x))

Techs = ['MIT', 'Caltech']
Ivys = ['Harvard', 'Yale', 'Brown']
Univs1 = [['MIT', 'Caltech'], ['Harvard', 'Yale', 'Brown']]
Univs = [Techs, Ivys]

print(id(Univs) == id(Univs1))
print("Univs id = ", id(Univs))
print("Univs1 id = ", id(Univs1))
print(Techs)
print(Ivys)
print(Univs)
"""

L1 = [1, 2, 3]
L2 = [4, 5, 6]
L3 = L1 + L2

print('L3 = ', L3)
L1.extend(L2)
print('L1 = ', L1)
L1.append(L2)
print('L1 = ', L1)

L = [1, 2, 3, 1, 5, 6]

e = 5

print("Index ", L.index(e))
L.sort()
print(L)
print("count ", e, "= ", L.count(1))
print(L)
K = [x ** 2 for x in range(1, 7)]
print("K = ", K)

def apply_to_each(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

def rev(x):
    return -x
L = [1, -2, 3.33]
print('L = ', L)
print('Apply abs to each')
apply_to_each(L, abs)
print('L = ', L)
print('Apply rev to each')
apply_to_each(L, rev)
print('L = ', L)

s = 'I <3 CS'
print(list(s))
print(s.split(' '))
L = ['a', 'b', 'c']
print(''.join(L))
print('*'.join(L))

L = [9, 6, 0, 3]
print(sorted(L))
L.sort()
print(L)

a = 1
b = a
print(a)
print(b)

# ALIAS
warm = ['red', 'yellow', 'orange']
hot = warm
hot.append('pink')
print('hot = ', hot)
print('warm = ', warm)
print()

# CLONING LIST
cool = ['blue', 'green', 'gray']
chill = cool[:]
chill.append('black')
print('chill = ', chill)
print('cool = ', cool)
print()

# SORTING LIST
warm = [2, -5, 0]
print('warm = ', warm)
warm.sort()
print('warm_sorted = ', warm)
print('sorted_warm = ', warm)

cool = [23, 0, -23]
sorted_cool = sorted(cool)
print('cool = ', cool)
print('sorted_cool = ', sorted_cool)
print()

# LIST OF LIST ...
warm = ['yellow', 'orange']
hot = ['red']
bright_color = [warm, hot]
print(bright_color)
hot.append('pink')
print(hot)
print(bright_color)






