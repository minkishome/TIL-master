def quuicksort(ls, l, r):
    if l < r:
        s = partition(ls, l, r)
        quuicksort(ls, l, s-1)
        quuicksort(ls, s+1, r)


def partition(ls, l, r):
    pivot = ls[r]
    i = l -1

    for j in range(l, r):
        if ls[j] <= pivot:
            i += 1
            ls[i], ls[j] = ls[j], ls[i]
    ls[i+1], ls[r] = ls[r], ls[i+1]
    return i+1


# def partition(ls, l, r):
#     p = ls[l]
#     i = l
#     j = r
#     while i < j:
#         while ls[i] <= p and i < r:
#             i += 1
#
#         while ls[j] >= p and j > l:
#             j -= 1
#         if i < j:
#             ls[i], ls[j] = ls[j], ls[i]
#
#     ls[l], ls[j] = ls[j], ls[l]
#     return j


ls3 = [3, 4, 7, 1, 5, 2, 4, 6, 8, 88, 134]
ls2 = [11, 45, 23, 81, 28, 34]
ls4 = [1,1,1,1,1,1,1,0,0,0,0]
ls5 = [11,45,22,81,23,34,99,22,17,8]
quuicksort(ls3, 0, len(ls3)-1)
quuicksort(ls2, 0, len(ls2)-1)
quuicksort(ls5, 0, len(ls5)-1)
quuicksort(ls4, 0, len(ls4)-1)
# print(ls3)
print(ls4, ls2, ls3, ls5)
# partition(ls2, 0, len(ls2)-1)
# print(ls2)