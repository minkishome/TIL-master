from collections import deque
import itertools
ls = deque((1,2,3))
print(ls)
a = ls.popleft()
print(a, ls)

lsls = [1,2,3,4]
cnt = 0
for k in lsls:
    cnt += 1
    if cnt < 10:
        lsls.append(5)
        print(k)
        print(lsls)
