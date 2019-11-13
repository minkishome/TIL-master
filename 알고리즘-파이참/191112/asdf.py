from itertools import permutations

idx = [[0, 1], [0, 2], [1, 2], [2, 1], [2, 3], [4, 0]]
power_set = [[]]
for i in idx:
    tmp = [[i] + p for p in power_set]
    power_set += tmp


for i in range(2**(len(idx))):
    print(power_set[i])
    print(power_set[-1-i])

lsls = [1,2,3,4]
ls = list(permutations(lsls))

print(ls)