import sys
sys.stdin = open('5208.txt', 'r')

def find(ls, i, cnt):
    global min_sum
    if i >= ls[0]:
        if cnt <= min_sum:
            min_sum = cnt
            return min_sum
    else:
        for z in range(i+1, i+1+ls[i]):
            if cnt+1 < min_sum:
                find(ls, z, cnt+1)



for tc in range(1, int(input())+1):
    ls =list(map(int,input().split()))

    min_sum = 999
    find(ls, 1, 0)
    print('#%d %d' %(tc, min_sum-1))