from itertools import combinations

def iswall(i,j):
    return 0 <= i < N and 0 <= j < M

N, M = map(int, input().split())
island = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
dxdy = [(1,0), (-1,0), (0,1), (0,-1)]
island_num = 0

stack = []
for i in range(N):
    for j in range(M):
        if island[i][j] == 1 and not visited[i][j]:
            island_num += 1
            stack = [(i,j)]
            while stack:
                kx, ky = stack.pop()
                if not visited[kx][ky]:
                    visited[kx][ky] = 1
                    island[kx][ky] = island_num
                    for dx, dy in dxdy:
                        nx = kx + dx
                        ny = ky + dy
                        if iswall(nx, ny) and not visited[nx][ny] and island[nx][ny]: # 범위 안 방문x 섬의 값 0 아닐때
                            stack.append((nx,ny))

# 다리 만들기
visited2 = [[0]*7 for _ in range(7)]
dxdy2 = [(1,0), (0,1)]
# print(visited2)
for x in range(N):
    for y in range(M):
        if island[x][y] != 0:
            for dx, dy in dxdy2:
                nx = x
                ny = y
                cnt = 0
                while 1:
                    nx += dx
                    ny += dy
                    if iswall(nx, ny) and island[nx][ny] == 0:
                        cnt += 1
                    elif iswall(nx, ny) and island[nx][ny] != island[x][y] and cnt != 1:
                        if visited2[island[x][y]][island[nx][ny]] == 0:
                            visited2[island[x][y]][island[nx][ny]] = cnt
                            break
                        else:
                            if visited2[island[x][y]][island[nx][ny]] > cnt:
                                visited2[island[x][y]][island[nx][ny]] = cnt
                                break
                    else:
                        break
         
make_bri = []

for i in range(island_num+1):
    for j in range(island_num+1):
        if j > i and visited2[i][j] != 0:
            make_bri.append([i,j,visited2[i][j]])
# print(make_bri)
min_value = 99999999999
for bri in combinations(make_bri, island_num-1):
    check = set()
    dis = 0
    for k in bri:
        check.add(k[0])
        check.add(k[1])
        dis += k[2]
    
    if len(list(check)) == island_num:
        if min_value > dis:
            min_value = dis
            # print(1, dis)

if min_value == 99999999999:
    print(-1)
else:
    print(min_value)