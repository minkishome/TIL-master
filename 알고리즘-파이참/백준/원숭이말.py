from collections import deque

def iswall(x, y):
    return 0 <= x < m and 0 <= y < n

# def move(i, j, cnt, horse_num):
#     global min_cnt
#     if cnt > min_cnt:
#         return
#     if i == n-1 and j == m-1:
#         if cnt < min_cnt:
#             min_cnt = cnt
#             return
#     else:
#         for k in range(2):
#             if k == 0:
#                 for q in dxdy:
#                     nx, ny = i + q[0], j + q[1]
#                     if iswall(nx,ny) and not visited[nx][ny] and arr[nx][ny] != 1:
#                         visited[nx][ny] = 1
#                         move(nx, ny, cnt+1, horse_num)
#                         visited[nx][ny] = 0
#             else:
#                 if horse_num < k: # 이때만 말처럼 이동
#                     for q in horse:
#                         nx, ny = i + q[0], j + q[1]
#                         if iswall(nx, ny) and not visited[nx][ny] and not arr[nx][ny] != 1:
#                             visited[nx][ny] = 1
#                             move(nx, ny, cnt + 1, horse_num + 1)
#                             visited[nx][ny] = 0

def move():
    q = deque()
    q.append((0, 0, 0))
    while q:
        x, y, z = q.popleft()
        num  = 4 if z == k else 12
        if x == m - 1 and y == n - 1:
            print(dist[x][y][z])
            return
        for i in range(num):
            nx, ny = x + dxdy[i][0], y + dxdy[i][1]
            if i < 4:
                nz = z
            else:
                nz = z + 1
            if 0 > nx or m <= nx or 0 > ny or ny >= n:
                continue
            if not arr[nx][ny] and not dist[nx][ny][nz]:
                dist[nx][ny][nz] = dist[x][y][z] + 1
                q.append((nx, ny, nz))

    print(-1)



k = int(input())
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
dist = [[[0] * (k+1) for _ in range(n)] for _ in range(m)]
dxdy = [(1, 0), (0, 1), (0, -1), (-1, 0), (2, 1), (1, 2), (-1, 2), (1, -2), (-2, -1), (-1, -2), (-2, 1), (2, -1)] # 4까지는 일반, 5부터 12까지는 말



move()