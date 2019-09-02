# def merge_sort(m):
#     if len(m) <= 1:
#         return m
#     mid = len(m) // 2
#     left = m[:mid]
#     right = m[mid:] # 계속해서 나눠주는 역할
#     left = merge_sort(left)
#     right = merge_sort(right)
#     return merge(left, right)
#
# def merge(left, right):
#     result = []
#     while len(left) > 0 and len(right) > 0:
#         if left[0] <= right[0]:
#             result.append(left.pop(0))
#         else:
#             result.append(right.pop(0))
#     if len(left) > 0:
#         result.extend(left)
#     if len(right) > 0:
#         result.extend(right)
#
#     return result
#
#
# ls = [69, 10, 30, 2, 16, 8, 31, 22]
# print(merge_sort(ls))
#

from collections import deque

d = deque([1, 5, 2, 4, 3])
h = deque([])
print(d)
h.appendleft(d.popleft())
def insertion_sort0(a):

while d:
    a = d.popleft()
    for i in h:
        if a < i:

