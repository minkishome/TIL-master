import sys
sys.stdin = open('exam4.txt','r')


def down(loca, i, j):
    if i == 99:
        return loca[i][j]             # 100일 경우 stop
    if j!=0:
        if loca[i][j-1] ==1:
            j -= 1
            return left(loca, i, j) # 먼저 좌우값이 1인지 판단.
    if j!=99:
        if loca[i][j + 1] == 1:
            j += 1
            return right(loca, i, j)
    if loca[i+1][j] == 1:
        i += 1
        return down(loca, i, j)

def left(loca, i, j):
    if loca[i+1][j] == 1:
        i += 1
        return down(loca, i, j)
    if j!=0:
        if loca[i][j-1] ==1:
            j -= 1
            return left(loca, i, j)


def right(loca, i, j):
    if loca[i+1][j] == 1:
        i += 1
        return down(loca, i, j)
    if j != 99:
        if loca[i][j+ 1] == 1:
            j += 1
            return right(loca, i, j)




for _ in range(10):
    numnum = int(input())
    ladder = []
    for i in range(100):
        PMK = list(map(int, input().split()))
        ladder.append(PMK)
    garo = 0   # i= 0, j=0에서 시작

    for sero in range(100):
        if ladder[garo][sero] == 1:
            a = down(ladder, garo, sero)
            if a == None:
                print('#%d %d' %(numnum, sero))

