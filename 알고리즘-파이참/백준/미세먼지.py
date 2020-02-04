import copy
def iswall(x,y):
    return 0<=x<R and 0<=y<C

R, C, T = map(int,input().split())

dust = [list(map(int, input().split())) for _ in range(R)]

air = []
#공기청정기 어딨는지 찾자
for k in range(R):
    if dust[k][0] == -1:
        air.append((k,0))
# 주변에 몇개인지 체크하고 그 숫자만큼 보내고 그런 식
dxdy = [(1,0),(-1,0),(0,1),(0,-1)]
time = 0
while time < T:
    dust_second = [ [0]*C for _ in range(R) ]
    for i in range(R):
        for j in range(C):
            # if (i-1,j) in air or (i+1,j) in air:
            #     sand = dust[i][j]
            #     if sand and sand != -1:
            #         cnt = 0
            #         for dx, dy in dxdy:
            #             x = i + dx
            #             y = j + dy
            #             if iswall(x,y) and sand != -1 and (x,y) not in air:
            #                 cnt += 1

            #                 dust_second[i][j] += int(sand / 5)
            #         dust_second[x][y] += (sand - int((cnt+1)*(sand//5)))
                 
            
            sand = dust[i][j]
            if sand and sand != -1:
                cnt = 0
                for dx, dy in dxdy:
                    x = i + dx
                    y = j + dy
                    if iswall(x,y) and  (x,y) not in air:
                        cnt += 1

                        dust_second[x][y] += int(sand / 5)
                dust_second[i][j] += (sand - int(cnt*(sand/5)))
    dust = dust_second
    # 공기청정기 이동
    dust_second = [ [0]*C for _ in range(R) ]
    # for k in air:
    k = air[0]
    l = air[1]
    for kk in range(k[0]-1,0,-1):
        dust[kk][0] = dust[kk-1][0]
    for kk in range(0,C-1):
        dust[0][kk] = dust[0][kk+1]
    for kk in range(0,k[0]-1):
        dust[kk][C] = dust[kk+1][C]
    for kk in range(C, 1,-1):
        dust[0][kk] = dust[0][kk-1]
    for ll in range(l[0], R-1):
        dust[ll][0] = dust[ll+1][0]
    for ll in range(0,C-1):
        dust[0][ll] = dust[0][ll+1]
    for ll in range(l[0]-1,0,-1):
        dust[ll][0] = dust[ll-1][0]
    for ll in range(C,1,-1):
        dust[0][ll] = dust[0][ll-1]
 
    dust[k[0]][0] = 0
    dust[l[0]][0] = 0


    time += 1

summ = 0
for k in dust:
    print(k)
    summ += sum(k)
answer = summ
print(answer)