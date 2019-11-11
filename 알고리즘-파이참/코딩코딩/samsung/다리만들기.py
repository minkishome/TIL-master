def iswall(x, y): return 0 <= x < N and 0 <= y < M

def how_many_island(ls):
    cnt = 1
    stack = []
    for i in range(N):
        for j in range(M):
            if ls[i][j] and not visited[i][j]:
                visited[i][j] = 1
                stack.append((i,j))
                while stack:
                    dx, dy  = stack.pop()
                    ls[dx][dy] = cnt
                    for dxdy in dxdys:
                        nx, ny = dx + dxdy[0], dy + dxdy[1]
                        if iswall(nx, ny) and ls[nx][ny] and not visited[nx][ny]:
                            visited[nx][ny] = 1
                            stack.append((nx,ny))
                ls_cnt.append(cnt)
                cnt += 1
    return cnt

def find():



N, M = map(int, input().split())
dxdys = [(1, 0), (0, 1), (-1, 0), (0, -1)]
dxdys2 = [(1,0),(0,1)]
land = [list(map(int, input().split())) for _ in range(N) ]
visited = [[0]*M for _ in range(N)]
ls_cnt = []
island = how_many_island(land)
for z in land:
    print(z)
land_bridge = [] # 다리만들어진 섬의 갯수
visited2 = [[0]*island for _ in range(island)]
print(visited2)
print(visited2[1][4])
# count_bridge = max(land)
for x in range(N):
    for y in range(M):
        if land[x][y] != 0:
            k = land[x][y]
            for alpha in dxdys2:
                nx, ny = x, y
                tmp = 0
                while 1:
                 # and land[nx][ny] == 0:
                    nx += alpha[0]
                    ny += alpha[1]
                    tmp += 1
                    if iswall(nx, ny):
                        if land[nx][ny] != k and land[nx][ny] != 0 and tmp != 1:
                            print(land[x][y], land[nx][ny])
                            if visited2[land[x][y]][land[nx][ny]] == 0:

                                visited2[land[x][y]][land[nx][ny]] = tmp
                                break
                            else:
                                if visited2[land[x][y]][land[nx][ny]] >= tmp:
                                    visited2[land[x][y]][land[nx][ny]] = tmp
                                    break
                    else:
                        break
print(visited2)
min_val = 99999
tmp_sum = 0
