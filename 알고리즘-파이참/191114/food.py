import sys
sys.stdin = open('food.txt', 'r')

def syer(ls):
    total = 0
    for i in ls:
        for j in ls:
            total += synerge[i][j]
    return total

import itertools
tc = int(input())
for tn in range(1,tc+1):
    N = int(input())
    N_list = list(range(N))
    synerge = [list(map(int,input().split())) for _ in range(N)]
    part = list(itertools.combinations(N_list, N//2))
    min_val = 999999
    l = len(part)
    for i in range(l//2):
        part1 = part[i]
        part2 = part[l-1-i]
        a = syer(part1)
        b = syer(part2)
        val = abs(a - b)
        if val < min_val:
            min_val = val
    print('#%d %d' %(tn, min_val))