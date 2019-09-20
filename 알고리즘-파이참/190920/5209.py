import sys
sys.stdin = open('5209.txt', 'r')

def find(ls, z, summ):
    global min_sum
    if z == n:
        if min_sum > summ:
            min_sum = summ
            return min_sum
    else:
        for i in range(n):
            if not check[i]:
                if summ + ls[z][i] < min_sum:
                    check[i] = True
                    find(ls, z+1, summ+ls[z][i])
                    check[i] = False





for tc in range(1, int(input())+1):
    n = int(input())
    ls = [list(map(int, input().split())) for _ in range(n)]
    min_sum = 909009090
    check = [0]*(n+1)
    find(ls, 0, 0)
    print('#%d %d' %(tc, min_sum))