from collections import deque

def iswall(x, y):
    return 0 <= x < N and 0 <= y < N



N = int(input())
land = [list(map(int,input().split())) for _ in range(N)]

max_land = 0
max_val = max(max(land))
dxdy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
rain = 0
while True:
    checked = []
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if land[i][j] > rain and not visited[i][j]:
                stack = []
                que = deque()
                stack.append((i, j))
                que.append((i, j))
                visited[i][j] = 1
                while que:
                    kk = que.popleft()
                    for xx in dxdy:
                        new_x, new_y = kk[0] + xx[0], kk[1] + xx[1]
                        if iswall(new_x, new_y) and not visited[new_x][new_y] and land[new_x][new_y] > rain:
                            visited[new_x][new_y] = 1
                            stack.append((new_x, new_y))
                            que.append((new_x, new_y))
                checked.append(stack)

    land_cnt = 0
    for i in checked:
        land_cnt += 1
    rain += 1
    # print(rain)
    if land_cnt > max_land:
        max_land = land_cnt

    if rain > max_val:
        break
print(max_land)