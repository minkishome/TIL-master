# from collections import deque
# def iswall(x, y):
#     return 0 <= x < r and 0 <= y < c
#
# def bfs(cnt):
#
#
#
#
# r, c = map(int, input().split())
# arr = [list(input()) for _ in range(r)]
# # #: 벽
# # .: 지나갈 수 있는 공간
# # J: 지훈이의 미로에서의 초기위치 (지나갈 수 있는 공간)
# # F: 불이난 공간
# visited = [[0]*c for _ in range(r)]
# dxdy = [(1,0), (0,1), (-1,0), (0,-1)]
#
#
# fire = deque()
#
#
# for i in range(r):
#     for j in range(c):
#         if arr[i][j] == 'J':
#             jx, jy = i, j
#         if arr[i][j] == 'F':
#             fire.append((i, j))
#             visited[i][j] = 1
#         if arr[i][j] == '#':
#             visited[i][j] = 1
# fire.append(jx, jy)


# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
#
# def bfs(x, y):
#     q.append([x, y])
#     c[x][y] = 1
#     while q:
#         qlen = len(q)
#         while qlen:
#             x, y = q.popleft()
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 if 0 <= nx < h and 0 <= ny < w:
#                     if a[nx][ny] == '.' and c[nx][ny] == 0:
#                         c[nx][ny] = c[x][y] + 1
#                         q.append([nx, ny])
#                 elif nx < 0 or ny < 0 or nx >= h or ny >= w:
#                     print(c[x][y])
#                     return
#             qlen -= 1
#         fire()
#
#     print("IMPOSSIBLE")
#     return
#
# def fire():
#     qlen = len(fq)
#     while qlen:
#         x, y = fq.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < h and 0 <= ny < w:
#                 if a[nx][ny] == '.':
#                     a[nx][ny] = '*'
#                     fq.append([nx, ny])
#         qlen -= 1
#
# w, h = map(int, input().split())
# a = [list(map(str, input().strip())) for _ in range(h)]
# fq, q = deque(), deque()
# c = [[0]*w for _ in range(h)]
# for i in range(h):
#     for j in range(w):
#         if a[i][j] == '@':
#             sx = i
#             sy = j
#             a[i][j] = '.'
#         if a[i][j] == '*':
#             fq.append([i, j])
# fire()
# bfs(sx, sy)

from collections import deque
def iswall(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs():
    global q
    while 1:
        q2 = deque()
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dxdy[i][0], y + dxdy[i][1]
                if iswall(nx, ny) and arr[nx][ny] == '.' and dist[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y] + 1
                    q2.append((nx, ny))
                elif not iswall(nx, ny):
                    print(dist[x][y])
                    return
        q = q2
        if not q:
            print('IMPOSSIBLE')
            return
        fire()



def fire():
    global f, f2
    while f:
        x, y = f.popleft()
        for i in range(4):
            nx, ny = x + dxdy[i][0], y + dxdy[i][1]
            if iswall(nx, ny) and arr[nx][ny] == '.':
                arr[nx][ny] = 'F'
                f2.append((nx, ny))
    f = f2
    f2 = deque()


n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

dxdy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
dist = [ [0]*m for _ in range(n)]
f = deque()
f2 = deque()
q = deque() # 위치 deque

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'J':
            sx, sy = i, j
            q.append((i,j))
            dist[i][j] = 1
        if arr[i][j] == 'F':
            f.append((i, j))
fire()
bfs()
