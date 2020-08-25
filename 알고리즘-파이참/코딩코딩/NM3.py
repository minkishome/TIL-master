# def find(lsls, z):
#     ls2 = lsls[:]
#     if z == M:
#         z = 0
#         for i in range(M - 1):
#             if lsls[i] <= lsls[i + 1]:
#                 z += 1
#         if z == M - 1:
#             for i in lsls:
#                 print(i, end= ' ')
#             print()
#     else:
#         for i in range(1, N+1):
#             ls2.append(ls[i])
#             find(ls2, z+1)
#             ls2.pop(-1)
#
#
#
# N, M = map(int,input().split())
# ls = [0] * (N+1)
# for i in range(1,N+1):
#     ls[i] = i
# visited = [False] * (N+2)
# ls3 = []
# find(ls3, 0)

import random

# def quickSort(x):
#     if len(x) <= 1:
#         return x
#     pivot = x[len(x)//2]
#     left,right,equal =[],[],[]
#     for a in x:
#         if a < pivot:
#             left.append(a)
#         elif a > pivot:
#             right.append(a)
#         else:
#             equal.append(a)
#     return quickSort(left) + equal + quickSort(right)
#
# ls = random.sample(range(1, 100), 5)
# print(ls)
# print(quickSort(ls))
# print(ls)


# def mergetSort(x):
#     if len(x) <= 1:
#         return x
#     left = mergetSort(x[:len(x)//2])
#     right = mergetSort(x[len(x)//2: ])
#
#     i,j,k = 0,0,0
#     while i<len(left) and j<len(right):
#         if left[i] < right[j]:
#             x[k] = left[i]
#             i += 1
#         else:
#             x[k] = right[j]
#             j += 1
#         k += 1
#     if i == len(left):
#         while j < len(right):
#             x[k] = right[j]
#             j += 1
#             k += 1
#         elif j == len(right):
#             while i < len(left):
#                 x[k] = left[i]
#                 i += 1
#                 k += 1
#     return x

def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    leftList = list[:mid]
    rightList = list[mid:]
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)
    return merge(leftList, rightList)


def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

ls = random.sample(range(1, 100), 5)
print(merge_sort(ls))