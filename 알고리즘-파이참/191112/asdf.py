idx = [[0, 1], [0, 2], [1, 2], [2, 1], [2, 3], [4, 0]]
power_set = [[]]
for i in idx:
    tmp = [[i] + p for p in power_set]
    power_set += tmp


for i in range(2**(len(idx))):
    print(power_set[i])
    print(power_set[-1-i])

ls = [3,1,4,5]
ls.sort()
print(ls)
