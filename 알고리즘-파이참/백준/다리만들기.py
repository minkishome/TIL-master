# from itertools import combinations
# #
# # def iswall(i,j):
# #     return 0 <= i < N and 0 <= j < M
# #
# # N, M = map(int, input().split())
# # island = [list(map(int,input().split())) for _ in range(N)]
# # visited = [[0]*M for _ in range(N)]
# # dxdy = [(1,0), (-1,0), (0,1), (0,-1)]
# # island_num = 0
# #
# # stack = []
# # for i in range(N):
# #     for j in range(M):
# #         if island[i][j] == 1 and not visited[i][j]:
# #             island_num += 1
# #             stack = [(i,j)]
# #             while stack:
# #                 kx, ky = stack.pop()
# #                 if not visited[kx][ky]:
# #                     visited[kx][ky] = 1
# #                     island[kx][ky] = island_num
# #                     for dx, dy in dxdy:
# #                         nx = kx + dx
# #                         ny = ky + dy
# #                         if iswall(nx, ny) and not visited[nx][ny] and island[nx][ny]: # 범위 안 방문x 섬의 값 0 아닐때
# #                             stack.append((nx,ny))
# #
# # # 다리 만들기
# # visited2 = [[0]*7 for _ in range(7)]
# # dxdy2 = [(1,0), (0,1)]
# # # print(visited2)
# # for x in range(N):
# #     for y in range(M):
# #         if island[x][y] != 0:
# #             for dx, dy in dxdy2:
# #                 nx = x
# #                 ny = y
# #                 cnt = 0
# #                 while 1:
# #                     nx += dx
# #                     ny += dy
# #                     if iswall(nx, ny) and island[nx][ny] == 0:
# #                         cnt += 1
# #                     elif iswall(nx, ny) and island[nx][ny] != island[x][y] and cnt != 1:
# #                         if visited2[island[x][y]][island[nx][ny]] == 0:
# #                             visited2[island[x][y]][island[nx][ny]] = cnt
# #                             break
# #                         else:
# #                             if visited2[island[x][y]][island[nx][ny]] > cnt:
# #                                 visited2[island[x][y]][island[nx][ny]] = cnt
# #                                 break
# #                     else:
# #                         break
# #
# # make_bri = []
# #
# # for i in range(island_num+1):
# #     for j in range(island_num+1):
# #         if j > i and visited2[i][j] != 0:
# #             make_bri.append([i,j,visited2[i][j]])
# # # print(make_bri)
# # min_value = 99999999999
# # for bri in combinations(make_bri, island_num-1):
# #     check = set()
# #     dis = 0
# #     for k in bri:
# #         check.add(k[0])
# #         check.add(k[1])
# #         dis += k[2]
# #
# #     if len(list(check)) == island_num:
# #         if min_value > dis:
# #             min_value = dis
# #             # print(1, dis)
# #
# # if min_value == 99999999999:
# #     print(-1)
# # else:
# #     print(min_value)

from collections import deque as dq

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

check = [[False]*n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans, k = 10**9, 1

def dfs(x, y):
    check[x][y] = True
    arr[x][y] = k
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if not check[nx][ny] and a[nx][ny]:
            dfs(nx, ny)

def bfs(z):
    global ans
    dist = [[-1]*n for _ in range(n)]
    q =dq()
    for i in range(n):
        for j in range(n):
            if a[i][j] == z:
                q.append((i,j))
                dist[i][j] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if a[nx][ny] and a[nx][ny] != z:
                ans = min(ans, dist[x][y])
                return
            if not a[nx][ny] and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
for i in range(n):
    for j in range(n):
        if not check[i][j] and a[i][j]:
            dfs(i, j)
            k += 1
for i in range(1, k+1):
    bfs(i)
print(ans)

