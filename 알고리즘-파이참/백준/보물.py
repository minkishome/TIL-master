import sys
from collections import deque
sys.stdin = open('보물.txt', 'r')


def find_dis(mapa, x, y, x1, y1, k, stack): # 최단 거리를 구해야한다. k = 이동한 거리
    global max_dis, min_dis, N, M, ls_dis2

    #언제 끝나나 두개 위치가 같을때 혹은 que에 값이 없을때? 물리적으로 이동이 불가능한 경우
    if x == x1 and y == y1:
        if min_dis > k:
            min_dis = k
            ls_dis2.append(min_dis)
            return ls_dis2 #둘 사이의 거리를 구해야한다.
    else:
        k += 1
        if k > min_dis:
            return
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        que = deque([])
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < N and 0 <= new_y < M: # 범위안에 있어야 함
                if mapa[new_x][new_y] != 'W':  # W가 아니면 스택에 넣는다?
                    if [new_x, new_y] not in stack: # 안 가본 점에 대해서 스택에 추가
                        stack.append([new_x, new_y])
                        que.append([new_x, new_y])
                        while que:
                            a = que.pop()
                            find_dis(mapa, a[0], a[1], x1, y1, k, stack)

                            # 여기서 내용을 더 추가해야함

        #for문을 다 돌고 while도 깨졌을 경우
        return   # 거리가 0이 나올 경우는 없으므로, 나중에 출력때 0이 아닐 경우를 생각






N, M  = map(int, input().split())
mapa = [list(input()) for _ in range(N)]
max_dis = 0
ls_land = deque([])
ls_dis1 = deque([])
for i in range(N):
    for j in range(M):
        if mapa[i][j] != 'W':
            ls_land.append([i,j])
distance = len(ls_land)
# print(distance)
print(ls_land)
# print(ls_land)
for i in range(distance-1):
    ls_dis2 = deque([])

    for j in range(i+1, distance):
        # print(j)
        min_dis = 1000  # 함수 while 내에서 최소 거리를 구한다.
        stack = deque([])
        l = 0
        dis = find_dis(mapa, ls_land[i][0], ls_land[i][1], ls_land[j][0], ls_land[j][1], l, stack)
        print(ls_land[i], ls_land[j])
        print(ls_dis2)
    if ls_dis2:
        a = min(ls_dis2)
        ls_dis1.append(a)


print(max(ls_dis1))
# print(ls_land)
# for i in range(N):
#     for j in range(M):
#         if mapa[i][j] == 'W':
#             continue
#         for u in range(N):
#             ls_dis2 = []
#             for k in range(M):
#                 if i == u and j == k:
#                     continue
#                 elif mapa[u][k] != 'W':
#                      # 두개가 물일때, 좌표가 같은 값일때는 패스
#                     min_dis = 1000  # 함수 while 내에서 최소 거리를 구한다.
#                     stack = []
#                     l = 0
#                     dis = find_dis(mapa, i, j, u, k, l, stack, ls_dis2)
#             if ls_dis2 != []:
#                 a = min(ls_dis2)
#                 ls_dis1.append(a)
#                 print([i,j], [u,k], ls_dis2)
# print(ls_dis1)


