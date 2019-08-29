def down(loca, i, j, c):
    if i == 99:
        return loca[i][j]               # 100일 경우 stop
    if j!=0:
        if loca[i][j-1] ==1:
            j -= 1
            c += 1
            return left(loca, i, j, c) # 먼저 좌우값이 1인지 판단.
    if j!=99:
        if loca[i][j + 1] == 1:
            j += 1
            return right(loca, i, j, c)
    if loca[i+1][j] == 1:
        i += 1
        return down(loca, i, j, c)

def left(loca, i, j):
    if loca[i+1][j] == 1:
        i += 1
        return down(loca, i, j, c)
    if j!=0:
        if loca[i][j-1] ==1:
            j -= 1
            return left(loca, i, j, c)




def right(loca, i, j):
    if loca[i+1][j] == 1:
        i += 1
        return down(loca, i, j)
    if j != 99:
        if loca[i][j+ 1] == 1:
            j += 1
            return right(loca, i, j)




for _ in range(10):
    count = 0
    numnum = int(input())
    ladder = []
    for i in range(100):
        PMK = list(map(int, input().split()))
        ladder.append(PMK)
    # 100x100 list 생성
    # 현재값 ==> location
    garo = 0   # i= 0, j=0에서 시작

    # while garo <= 100:
    #     if ladder[0][sero] == 1:
    #         location = ladder[0][garo]
    #     else:
    #         j += 1
    # 시작점 찾기

    for sero in range(100):
        if ladder[garo][sero] == 1:
            a = down(ladder, garo, sero)
            if a == None:
                print('#%d %d' %(numnum, sero))