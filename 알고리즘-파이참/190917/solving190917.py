import sys
sys.stdin = open('solving190917.txt', 'r')

def makemake(z, summ):
    global max_value
    if z == n:
        if max_value < summ:
            max_value = summ

    else:
        for i in range(n):
            if not visited[i]:
                if max_value < summ*ls[z][i]*0.01:
                    visited[i] = True
                    makemake(z+1, summ*ls[z][i]*0.01)
                    visited[i] = False





for tc in range(1, int(input()) + 1):
    n = int(input())
    max_value = 0
    ls = [list(map(int, input().split())) for _ in range(n)]

    visited = [False] * (n+1)
    makemake(0, 1)
    round(max_value, 6)
    print('#%d %f' %(tc, max_value*100))
