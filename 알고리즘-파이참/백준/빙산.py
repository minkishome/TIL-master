# from collections import deque
#
# def iswall(x, y):
#     return 0 <= x < n and 0 <= y < m
#
# def stack(i, j):
#     visited = [[0]*m for _ in range(n)]
#     q = deque()
#     q.append((i,j))
#     cnt = 0
#     while q:
#         x, y = q.popleft()
#         visited[x][y] = 1
#         for k in range(4):
#             nx = x + dxdy[k][0]
#             ny = y + dxdy[k][1]
#             if iswall(nx, ny) and arr[nx][ny] != 0 and not visited[nx][ny]:
#                 q.append((nx, ny))
#                 cnt += 1
#     return cnt
#
#
# n, m = map(int, input().split())
#
# arr = [list(map(int, input().split())) for _ in range(n)]
# dxdy = [(1,0), (0,1), (-1,0), (0,-1)]
#
# arr_check = [[[0]*5 for _ in range(m)] for _ in range(n)]
# check = []
# # cnt_ice = 0
# for i in range(n):
#     for j in range(m):
#         if arr[i][j] != 0:
#             check.append((i,j))
#             # cnt_ice += 0
#             for k in range(4):
#                 nx, ny = i + dxdy[k][0], j + dxdy[k][1]
#                 if iswall(nx, ny) and arr[nx][ny] != 0:
#                     arr_check[i][j][0] = 0
#                     arr_check[i][j][k + 1] = (nx,ny)
# flag = True
# time = 0
# while flag:
#     time += 1
#     for i in range(n):
#         for j in range(m):
#             if arr[i][j] > 0:
#                 cnt_icecube = 0
#                 for k in range(4):
#                     if arr_check[i][j][k+1] != 0:
#                         if arr[arr_check[i][j][k+1][0]][arr_check[i][j][k+1][1]] <= 0:
#                             cnt_icecube += 1
#                 arr_check[i][j][0] = cnt_icecube
#     cnt_oce = 0
#     for i in range(n):
#         for j in range(m):
#             if arr[i][j] != 0:
#                 arr[i][j] -= arr_check[i][j][0]
#                 if arr[i][j] > 0:
#                     cnt_oce += 1
#     for k in check:
#         if arr[k[0]][k[1]] > 0:
#             qqq = stack(k[0], k[1])
#             if cnt_oce != qqq:
#                 flag = False
# print(time)
#
from collections import deque

def iswall(x,y):
    return 0 <= x < n and 0 <= y < m

def count_sea():
    global arr
    list_ice = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0:
                cnt = 0
                list_ice.append((i, j))
                for k in range(4):
                    nx, ny = i + dxdy[k][0], j + dxdy[k][1]
                    if iswall(nx, ny) and arr[nx][ny] <= 0:
                        cnt += 1
                check[i][j] = cnt # 빼줄 값을 넣는다
    for q in list_ice:
        arr[q[0]][q[1]] -= check[q[0]][q[1]]

def count_ice():
    visited = [[0]*m for _ in range(n)]
    stack = deque()
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0 and not visited[i][j]:
                visited[i][j] = 1
                cnt += 1
                stack.append((i, j))
                while stack:
                    x, y = stack.popleft()
                    for k in range(4):
                        nx, ny = x + dxdy[k][0], y + dxdy[k][1]
                        if iswall(nx, ny) and arr[nx][ny] > 0 and not visited[nx][ny]:
                            stack.append((nx, ny))
                            visited[nx][ny] = 1
    return cnt # cnt가 2이상이면 분리됨, 0일 경우는 분리되지 않는경우



n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
check = [[0] * m for _ in range(n)]
# 먼저 주변에 바다가 몇개인지 확인하고 빼주고 빙하가 총 몇개인지 확인

dxdy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

flag = True
cnt = 0
while flag:
    cnt += 1
    count_sea() # arr 변화
    icy = count_ice()
    if icy > 1:
        flag = False
        # break
    elif icy == 0:
        flag = False
        cnt = 0
        # break

print(cnt)