import sys, copy
sys.stdin = open('comeon.txt', 'r')

def find(z, summ):
    global min_sum, cnt
    if z == M:
        if summ < min_sum:
            min_sum = summ
            return min_sum
    else:
        while 1:
            cnt += 1
            for i in range(N):
                ls2[i] -= 1
                if ls2[i] == 0:
                    new_summ = summ+ls[i]






for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    ls = [0] + [int(input()) for _ in range(N)]
    ls2 = copy.deepcopy(ls)
    cnt = 0
    min_sum = 9090909090
    check = [False] * (N+1)

    print('#%d %d' %(tc, check))