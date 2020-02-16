import copy
from collections import deque
def iswall(x,y):
    return 0<=x<n and 0<=y<m


# 이거는 DFS로 해서 시간 초과 임
# def move(a, pointed, cnt, visited):
#     global min_value
#     # 방향 바꾸는거 하나 이동하는 거 하나
#     if cnt > min_value:
#         return
#     if a == 0: #방향을 바꾼다
#         for k in range(0, 4):
#             if k != pointed[2]:
#                 pointed[2] = k
#                 move(1, pointed, cnt+1, visited)
#             else: # 방향 변화가 없음을 의미
#                 move(1, pointed, cnt, visited) # 방향이 같은 경우에는 cnt를 더할 필요가 없다.
#     elif a == 1:
#         visited2 = copy.deepcopy(visited)
#         for k in range(1, 4): # 1부터 3까지 이동할 수 있다.
#             point = pointed.copy()
#             new_x, new_y = point[0] + dir[point[2]][0]*k, point[1] + dir[point[2]][1]*k
#             if iswall(new_x, new_y)  and not visited2[new_x][new_y]:
#                 if arr[new_x][new_y] != 1:
#                     point[0], point[1] = new_x, new_y
#                     visited2[new_x][new_y] = 1
#                     if point[0] == last[0] and point[1] == last[1]:
#                         if point[2] == last[2]:
#                             if min_value > cnt + 1:
#                                 min_value = cnt+1
#                         else:
#                             if min_value > cnt+2:
#                                 min_value = cnt+2
#                     else:
#                         move(0, point, cnt+1, visited2)
#                 else:
#                     return

def bfs():
    q = deque()
    q.append((init[0], init[1], init[2]))
    while q:
        x, y, d = q.popleft()
        if x == last[0] and y == last[1] and d == last[2]:
            print(dist[x][y][d])
            return
        for i in range(1, 4):
            nx, ny = x + dir[d][0]*i, y + dir[d][1]*i
            # if iswall(nx, ny) and arr[nx][ny] != 1:
            #     break
            # if not dist[nx][ny][d]:
            #     q.append((nx, ny, d))
            #     dist[nx][ny][d] = dist[x][y][d] +1
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                break
            if arr[nx][ny]:
                break
            if not dist[nx][ny][d]:
                q.append((nx, ny, d))
                dist[nx][ny][d] = dist[x][y][d] + 1


        for i in range(4):
            if i == d:
                continue
            k = 2 if (i + d) % 4 == 1 else 1
            if not dist[x][y][i]:
                q.append((x, y, i))
                dist[x][y][i] = dist[x][y][d] + k





n, m = map(int,input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
init = list(map(int, input().split())) # [x, y, dir]
last = list(map(int, input().split()))
for k in range(3):
    init[k] -= 1
    last[k] -= 1
# dir = 동 서 남 북 (1, 2, 3, 4)

dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
min_value = 1000
visit = [[0]*m for _ in range(n)]
visit[init[0]][init[1]] = 1
dist = [[[0]*4 for _ in range(m)] for _ in range(n)]
# dist[init[0]][init[1]][init[2]] = 0
# print(min_value)
bfs()
