from collections import deque
import itertools
ls = deque((1,2,3))
print(ls)
a = ls.popleft()
print(a, ls)

lsls = [1,2,3,4]

ls2 = list(itertools.combinations(lsls,2))
print(ls2)
ls3 = list(itertools.permutations(lsls,2))
print(ls3)