#
# def find_pos_aux(v, mList):
#     """
#     Find right position of v in the pre-sorted list l
#     """
#     low, high = 0, len(mList) - 1
#     mid = (low + high) // 2
#     #print('high = ', high, 'low = ', low, 'mid = ', mid)
#     while high > low + 1:
#         if v == mList[mid]:
#             break
#         elif v > mList[mid]:
#             low = mid
#         else:
#             high = mid
#         mid = (low + high) // 2
#
#     # pint('# val = ', v, ' | mid1 = ', mid + 1, end=' | ')
#     '''
#     if mid == 0:
#         return mid
#     if mid == len(mList) - 2:
#         mid += 2
#     '''
#     return mid + 1
#
# def find_pos(v, L):
#     if len(L) == 0 or v < L[0]:
#         #print('empty')
#         pos = 0
#         return pos
#     elif v > L[len(L) - 1]:
#         #print('at tail')
#         pos = len(L)
#         #print('LEN = ', len(L))
#     else:
#         pos = find_pos_aux(v, L)
#     return pos
#
#
# def insert(v, fL):
#     # print('right_pos = ', find_pos_aux(v, fL))
#     fL.insert(find_pos(v, fL), v)
#
#
# # mList = []
# # e = 1
# # insert(e, mList)
# # print('mList = ', mList)
# #
# # e = 3
# # insert(e, mList)
# # print('mList = ', mList)
# #
# # e = 4
# # insert(e, mList)
# # print('mList = ', mList)
# #
# # e = -12
# # insert(e, mList)
# # print('mList = ', mList)
# #
# # e = 13
# # insert(e, mList)
# # print('mList = ', mList)
#
#
# # print('TESTING ............')
# # iList = [1, 3, 4, 60, 70, 50, 2]
# #
# #
# # mList = []
# # for e in iList:
# #     insert(e, mList)
# #     print('mList = ', mList)
#
# # mList.insert(0, 1)
# # for e in iList:
# #     if e < mList[0]:
# #         mList.insert(0, e)
# #     elif e > mList[len(mList) - 1]:
# #         mList.insert(len(mList) - 1, e)
# #     else:
# #         mList.insert(find_pos(e, mList), e)
# #     print('mList = ', mList)
# #
# # print('mList = ', mList)
# # exit(0)
#
#
# rList = []
# # cnt = 0
# while True:
#     try:
#         x = int(input())
#         insert(x, rList)
#         # cnt += 1
#         # print('Case ', cnt, ': ',)
#         # print('List = ', rList)
#         if len(rList) % 2 == 0:
#             ans = (rList[len(rList) // 2 - 1] + rList[len(rList) // 2]) // 2
#         else:
#             ans = rList[len(rList) // 2]
#         print(ans)
#     except EOFError:
#         break

""" Lecture 10: Program Efficiency """

import time

def fib(n):
    if n <= 1:
        return 1
    return n * fib(n - 1)

# start timer
start_time = time.clock()

# function executive duration
n = 800
fib(n)

# stop timer
finished_time = time.clock()

# taken time

taken_time = finished_time - start_time

print('start time: ', round(start_time, 5), '| finished time: ',
      round(finished_time, 5), ' | taken time: ', round(taken_time, 5))


# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 11:27:54 2016

@author: ericgrimson
"""

def linear_search(L, e):
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
    return found

testList = [1, 3, 4, 5, 9, 18, 27]

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


def isSubset(L1, L2):
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True


testSet = [1, 2, 3, 4, 5]
testSet1 = [1, 5, 3]
testSet2 = [1, 6]

def intersect(L1, L2):
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)
    res = []
    for e in tmp:
        if not(e in res):
            res.append(e)
    return res
