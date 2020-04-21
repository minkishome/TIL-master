M, N, H = map(int, input().split())
tomato = [[] for _ in range(H)]
for k in range(H):
    ls = [list(map(int, input().split())) for _ in range(N)]
    tomato[k] = ls
# 토마토 모두 배열에 넣음 1 = 익은 토마토 0 익지않은 토마토 -1 토마토 없음

dxdy = ((0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0))

while True:
    stack_1 = [] # 익은 토마토
    stack_0 = [] # 안 익은 토마토
    for h in range(H):
        for y in range(N):
            for x in range(M):
                if tomato[h][y][x] == 1:
                    stack_1.append((h, y, x))
    for k in dxdy:
        for z in stack_1:
            if 0 < k[0] + z[0] < H and 0 < k[1] + z[1] < N and 0 < k[2] + z[2] < M and tomato[k[0] + z[0]][k[1] + z[1]][k[2] + z[2]] == 0:
                tomato[k[0] + z[0]][k[1] + z[1]][k[2] + z[2]] = 1
