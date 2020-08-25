# # inputs = list(input().split(' '))
# inputs = list(map(int,input().split(' ')))
#
#
# ls_num =[
#     [8,0], [7,1], [2,2], [4,3], [3,4], [1,5], [6,6], [5,7], [0,8],
#     [9,1]
# ]
# ls_compare = []
# for i in inputs:
#     ls_compare.append(ls_num[i])
# ls_compare = sorted(ls_compare)
#
# answer = []
# for i in ls_compare:
#     answer.append(str(i[1]))
# anw = ' '.join(answer)
# print(anw)
# # def quick(x):
#     # if len(x) <= 1:
#     #     return x
#     # left, right, same = [], [], []
#     # pivot = ls_compare[len(x)//2][1]
#     # for a in x:
#     #     if a > pivot:
#     #         left.append(a)
#     #     elif a < pivot:
#     #         right.append(a)
#     #     else:
#     #         same.append(a)
#     # return quick(left) + quick(same) + quick(right)
#
# # print(quick(inputs))
from ast import literal_eval

a, b = map(list, input().split('/'))

a.pop()
a.pop(0)
# print(a)
a = ''.join(a)
print(a)
# print(a)

d = literal_eval(a)
print(d)
# dictionary = literal_eval(a)
# dic = eval(a)
# print(dic)



