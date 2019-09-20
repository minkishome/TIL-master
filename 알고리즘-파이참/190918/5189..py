import sys
sys.stdin = open('5189.txt', 'r')

def find_min(x, summ, z):
    global min_sum
    if z == n-1:
        if min_sum > summ + ls[x][0]:
            min_sum = summ + ls[x][0]
    elif summ < min_sum:
        for i in range(n):
            if not visited[i] and ls[x][i] != 0:
                visited[i] = True
                find_min(i, summ + ls[x][i], z + 1)
                visited[i] = False





for tc in range(1, int(input())+1):
    n = int(input())
    ls = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * (n+1)
    visited[0] = True
    stack = [1]

    min_sum = 99999
    for k in range(0, n):
        find_min(0, k, 0)
    print('#%d %d' %(tc, min_sum))