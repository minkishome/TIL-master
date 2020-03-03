from collections import deque
#
# def iswall(x, y):
#     return 0 <= x < r and 0 <= y < c
#
# def is_ice():
#     arr2 = []
#     for i in range(r):
#         for j in range(c):
#             if arr[i][j] == 'X':
#                 for k in dxdy:
#                     x, y = i + k[0], j + k[1]
#                     if iswall(x,y) and arr[x][y] == '.':
#                         arr2.append((i, j))
#                         break
#     for k in arr2:
#         arr[k[0]][k[1]] = '.' # arr2에 있는 모든 점을 '.'으로 바꾼다.
#
# def couldgo(x, y, lx, ly):
#     visited = [[0]*c for _ in range(r)]
#     visited[x][y] = 1
#     q = deque()
#     q.append((x, y))
#     while q:
#         xx, yy = q.popleft()
#         for k in dxdy:
#             nx, ny = xx + k[0], yy + k[1]
#             if nx == lx and ny == ly:
#                 return 1
#             if iswall(nx, ny) and arr[nx][ny] == '.' and not visited[nx][ny]:
#                 visited[nx][ny] = 1
#                 q.append((nx, ny))
#     return -1
#
#
#
# r, c = map(int, input().split())
# arr = [list(input()) for _ in range(r)]
#
# dxdy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#
# swan = []
# for i in range(r):
#     for j in range(c):
#         if arr[i][j] == 'L':
#             swan.append((i, j))
# day = 0
# while 1:
#     day += 1
#     is_ice()
#     # for k in arr:
#     #     print(k)
#     # print('---------------------------------------------------------------------')
#     res = couldgo(swan[0][0], swan[0][1], swan[1][0], swan[1][1])
#     if res == 1:
#         break
#
# print(day)

ex, ey, ans = 0, 0, 0
dx, dy = (0, -1, 0, 1), (-1, 0, 1, 0)
R, C = map(int, input().split())
a = [list(input()) for _ in range(R)]
wc = [[False]*C for _ in range(R)]
sc = [[False]*C for _ in range(R)]
wq1, wq2 = deque(), deque()
sq1, sq2 = deque(), deque()

def water():
    while wq1:
        x, y = wq1.popleft()
        a[x][y] = '.'
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C or wc[nx][ny]:
                continue
            if a[nx][ny] == '.':
                wq1.append((nx, ny))
            else:
                wq2.append((nx, ny)) # 다음 날 물이 될 지역
            wc[nx][ny] = True


def swan():
    while sq1:
        x, y = sq1.popleft()
        if x == ex and y == ey:
            return True
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C or sc[nx][ny]:
                continue
            if a[nx][ny] == '.':
                sq1.append((nx, ny))
            else:
                sq2.append((nx, ny))
            sc[nx][ny] = True
    return False

for i in range(R):
    for j in range(C):
        if a[i][j] == 'L':
            if not sq1:
                sq1.append((i, j))
                sc[i][j] = True
            else:
                ex, ey = i, j # 두번째 백조
            a[i][j] = '.'
        if a[i][j] == '.':
            wq1.append((i, j))
            wc[i][j] = True

while True:
    water()
    if swan():
        break
    wq1 = wq2
    sq1 = sq2
    wq2 = deque()
    sq2 = deque()
    ans += 1
print(ans)

