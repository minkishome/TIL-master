import sys
sys.stdin = open('5205.txt', 'r')

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

for tc in range(1, int(input())+1):
    N = int(input())
    ls = list(map(int, input().split()))
    quuicksort(ls, 0, N-1)
    print('#%d %d' %(tc, ls[N//2]))