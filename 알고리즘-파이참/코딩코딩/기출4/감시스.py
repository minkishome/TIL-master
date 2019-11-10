# 1 : 1방향 2: 양방향 3: 90도 4 : 3방향 5 : 전체
def iswall(x,y):
    return 0 <= x < N and 0 <= y < M and office[x][y] != 6

def cctv(depth, k_cnt):
    global cnt
    if depth == len(cctv_location):
        cnt = min(cnt, k_cnt)

    else:
        camera, kx, ky = cctv_location[depth]
        dxdys = dir[camera]
        for dxdy in dxdys:
            tmp = []
            for dx, dy in dxdy:
                nx, ny = kx, ky
                while True:
                    nx, ny = nx + dx, ny + dy
                    if iswall(nx, ny):
                        if office[nx][ny] == 0:
                            tmp.append((nx,ny))
                            office[nx][ny] = 7
                    else:
                        break
            cctv(depth+1, k_cnt-len(tmp)) # 추가한 거리만큼 cnt(0의 갯수)를 빼준다.
            for bx, by in tmp:
                office[bx][by] = 0




N, M = map(int, input().split())
cnt = 0
office = [list(map(int, input().split())) for _ in range(N) ]
cctv_location = []
# cctv 위치를 받고 그걸 어떻게
for i in range(N):
    for j in range(M):
        if office[i][j] == 0:
            cnt += 1
        elif office[i][j] == 5:
            for k in range(N):
                if office[k][j] == 0:
                    office[k][j] = 7
            for k in range(M):
                if office[i][k] == 0:
                    office[i][k] = 7

        elif office[i][j] and office[i][j] not in [7, 6]:
            if office[i][j] != 5:
                cctv_location.append([office[i][j], i, j ])

print(cnt)

change = [1, -1]

for z in office:
    print(z)
print(cctv_location)


dir = [[],
       [[(0, 1)], [(0, -1)], [(1, 0)], [(-1, 0)]],
       [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]],
       [[(0, 1), (-1, 0)], [(0, 1), (1, 0)], [(0, -1), (1, 0)], [(-1, 0), (0, -1)]],
       [[(0, -1), (-1, 0), (0, 1)], [(-1, 0), (0, 1), (1, 0)],
          [(0, 1), (1, 0), (0, -1)], [(1, 0), (0, -1), (-1, 0)]]]

cctv(0, cnt)
print(cnt)