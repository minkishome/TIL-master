import collections
import itertools
import queue
# ls = deque((1,2,3))
# print(ls)
# a = ls.popleft()
# print(a, ls)
#
# lsls = [1,2,3,4]
# cnt = 0
# for k in lsls:
#     cnt += 1
#     if cnt < 10:
#         lsls.append(5)
#         print(k)
#         print(lsls)

lslsls = [1,2,3,4,5] # ,6,7,8,9,10,11,12,13,14,15,16,17,18]

ls2 = itertools.combinations(lslsls, 3)
ls3 = itertools.permutations(lslsls, 3)
ls4 = itertools.combinations_with_replacement(lslsls, 3)
print(ls2)
for i in ls2:
    print(i)
for j in ls3:
    print(j)

print('////////////////////////////')
for k in ls4:
    print(k)
# for k in ls2:
#     print(k)
# ls3 = itertools.permutations(lslsls,3)
T = [1,2,3,4,4,4,5,5,2,1,2,3]
for S1 in T:
    S2 = [x for x in A if x not in S1]
