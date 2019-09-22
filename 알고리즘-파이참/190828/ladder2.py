def down(loca, i, j, c, m):
    c += 1
    if i == 99:
        if loca[i][j] == 1:

            return c# 100일 경우 stop

    if j!=0:
        if loca[i][j-1] ==1:
            j -= 1
            return left(loca, i, j, c, m) # 먼저 좌우값이 1인지 판단.
    if j!=99:
        if loca[i][j + 1] == 1:
            j += 1
            return right(loca, i, j, c, m)
    if loca[i+1][j] == 1:
        i += 1
        return down(loca, i, j, c, m)

def left(loca, i, j, c, m):
    c += 1
    if loca[i+1][j] == 1:
        i += 1
        return down(loca, i, j, c, m)
    if j!=0:
        if loca[i][j-1] ==1:
            j -= 1
            return left(loca, i, j, c, m)

def right(loca, i, j, c, m):
    c += 1
    if loca[i+1][j] == 1:
        i += 1
        c += 1
        return down(loca, i, j, c, m)
    if j != 99:
        if loca[i][j+ 1] == 1:
            j += 1
            return right(loca, i, j, c, m)



import sys
sys.stdin = open('ladder2.txt', 'r')

for _ in range(10):
     # 여기서 더한다.
    min_value = 99999
    numnum = int(input())
    ladder = []
    for i in range(100):
        PMK = list(map(int, input().split()))
        ladder.append(PMK)

    garo = 0   # i= 0, j=0에서 시작

    # while garo <= 100:
    #     if ladder[0][sero] == 1:
    #         location = ladder[0][garo]
    #     else:
    #         j += 1
    # 시작점 찾기

    # ls_count = []
    mincnt = 1000
    for sero in range(100):
        if ladder[garo][sero] == 1:
            count = 0
            a = down(ladder, garo, sero, count, min_value)
            # ls_count.append([a,sero])

            if a <= mincnt:
                mincnt = a
                result = sero

    # print(result)

    # for i in range(len(ls_count)-1,0,-1):
    #     min_idx = i
    #     for j in range(i,-1,-1):
    #         if ls_count[min_idx][0] < ls_count[j][0]:
    #             min_idx = j
    #         # if ls_count[min_idx][0] == ls_count[j][0]:
    #         # if ls_count[min_idx][0] == ls_count[j][0]:
    #         #     ls_count[min_idx], ls_count[j] = ls_count[j], ls_count[min_idx]
    #     ls_count[min_idx], ls_count[i] = ls_count[i], ls_count[min_idx]
    # print(ls_count)

    print('#%d %d' %(numnum, result))