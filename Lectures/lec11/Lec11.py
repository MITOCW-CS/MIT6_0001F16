# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 12:13:13 2016

@author: ericgrimson
"""

import random

l = []
for i in range(1, 100):
    l.append(random.randint(1, 100))
# print('LEN = ', len(l))
# print(l)

def lsearch(v, mList):
    rs = []
    for i in range(0, len(mList)):
        if v == mList[i]:
            print('i = ', i)
            rs.append(i)
    return rs
def bsearch(v, mList):
    low, high = 0, len(mList) - 1
    mid = (low + high) // 2
    while high > low:
        if v == mList[mid]:
            print('mid = ', mid)
            return mid
        if v > mList[mid]:
            low = mid
        else:
            high = mid
        mid = (low + high) // 2
    return False

def test(v, mList):
    if bsearch(v, mList) not in lsearch(v, mList):
        print('Failed!')
    print('Passed!')

testList = [21, 60, 16, 42, 18, 51, 32, 96, 60, 1, 51, 52, 1, 71, 9, 80, 89, 30, 22, 59, 29, 73, 38, 32, 19, 48, 1, 81, 14, 27, 6, 85, 34, 95, 98, 37, 56, 20, 10, 97, 88, 80, 91, 98, 63, 34, 4, 62, 69, 27, 54, 6, 36, 69, 69, 96, 69, 76, 62, 5, 73, 27, 30, 94, 64, 68, 35, 15, 80, 76, 19, 53, 92, 7, 40, 64, 83, 66, 93, 43, 40, 1, 88, 67, 46, 37, 8, 100, 19, 28, 27, 12, 64, 69, 30, 17, 38, 53, 61]
testList.sort()
v = 21
test(v, testList)
exit(0)

def bisect_search2(L, e):
    def bisect_search_helper(L, e, low, high):
        print('low: ' + str(low) + '; high: ' + str(high))  # added to visualize
        if high == low:
            return L[low] == e
        mid = (low + high) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:  # nothing left to search
                return False
            else:
                return bisect_search_helper(L, e, low, mid - 1)
        else:
            return bisect_search_helper(L, e, mid + 1, high)

    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L) - 1)


testList = []
for i in range(100):
    testList.append(i)

print(bisect_search2(testList, 76))


def genSubsets(L):
    res = []
    if len(L) == 0:
        return [[]]  # list of empty list
    smaller = genSubsets(L[:-1])  # all subsets without last element
    extra = L[-1:]  # create a list of just last element
    new = []
    for small in smaller:
        new.append(small + extra)  # for all smaller solutions, add one with last element
    return smaller + new  # combine those with last element and those without


testSet = [1, 2, 3, 4]
print(genSubsets(testSet))

###########################3


