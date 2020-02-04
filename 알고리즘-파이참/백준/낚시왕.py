def iswall(x, y):
    return 0 <= x < r and 0 <= y < c

def shark_move(k, summm):
    if k == c:
        return summm
    else:
        # goto = 1
        for shark in info_shark:#shark[2] =속도 shark[3] = 방향 shark[4] = 크기 나눠서 몫이 홀수면 같은 방향 짝수면 반대방향
            turn = shark[2] # 0이 될때까지
            for a in range(turn):
                shark[0] += direc[shark[3]][0]
                if shark[3] == 1 or 2:
                    if shark[0] == 0 and shark[3] == 1:
                        shark[3] = 2
                    elif shark[0] == r and shark[3] == 2:
                        shark[3] = 1
            else: # 3, 4 위아래
                shark[1] += direc[shark[3]][0]
                if shark[3] == 3 or 4:
                    if shark[1] == 0 and shark[3] == 4:
                        shark[3] = 3
                    elif shark[1] == c and shark[3] == 3:
                        shark[3] = 4

        min_dis = 999
        for qq in range(len(info_shark)):
            if info_shark[qq][1] == k:
                if min_dis > qq:
                    min_dis = qq
        if min_dis != 999:
            summm += info_shark[min_dis][4]
        return shark_move(k+1, summm)
#     return min_dis(info_shark, k, summm) # min_dis로 보내야한다.


# # 열에서 가장 가까운 상어를 잡는다.
# def min_dis(shark, people, summ):
#     min_dis = 999
#     for k in range(len(shark)):
#         if shark[k][1] == people:
#             if min_dis > k:
#                 min_dis = k
#     if min_dis != 999:
#         summ += shark[min_dis][4]
#     return shark_move(k+1, summ)


r, c, m = map(int,input().split())

info_shark = [list(map(int, input().split())) for _ in range(m)] # r,c,s,d,z = (r,c) speed, direction, z는 크기 같은 위치 큰게 작은거 먹는다.
water_tank = [ [0]*c for _ in range(r) ]
shark = [0]*m # 이거 왓다갓다 하면서 낚시
direc = [0, (-1,0), (1,0), (0,1), (0,-1)] # 1,2,3,4 위,아래,오,왼,

# i = 0
# for k in info_shark:
#     water_tank[k[0]][k[1]] = i
#     i += 1 # 사실 필요없을듯
# #infor shark와 연결되어있음

for k in info_shark:
    if k[3] == 1 or k[3] == 2:
        if k[4] >= 2*(r-1):
            k[4] = k[4] %(2*(r-1))
    else:
        if k[4] >= 2*(c-1):
            k[4] = k[4] % (2*(c-1))

# 나머지로 계산해서 속도를 높인다.
    
summ_shark = shark_move(0,0)
print(summ_shark)