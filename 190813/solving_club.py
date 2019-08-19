def garo_sero(A):

    garo = [0] * 100
    sero = [0] * 100
    for j in range(100):
        a = 0
        b = 0
        for i in range(100):
            a += A[i][j]
            b += A[j][i]
        garo[j] = a
        sero[j] = b
    result = max(max(garo), max(sero))

    return result


def diagonal(A):
    a = 0
    b = 0

    for i in range(100):
        a += A[i][i]
        b += A[i][100 - 1 - i]
    result = max(a,b)
    return result

import sys
sys.stdin = open('solving_club.txt','r')

for tc in range(10):
    T = int(input())
    club = []
    for i in range(100):
        KNM = list(map(int, input().split()))
        club.append(KNM)

    print('#%d %d'%(tc+1, max(garo_sero(club), diagonal(club))))