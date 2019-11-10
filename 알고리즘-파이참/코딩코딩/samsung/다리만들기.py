def iswall(x, y): return 0 <= x < N and 0 <= y < M

def how_many_island(ls):
    cnt = 1
    dxdys = [(1,0), (0,1), (-1,0), (0,-1)]
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
                cnt += 1


def make_dari(depth, cnt, land_ls):
    global min_val
    if depth == count_bridge: # 완전탐색해서 모두 연결 되어있는지
        if len(land_ls) == ls_cnt:
            if min_val > cnt:
                min_val = cnt
                return
    else:
        for

    pass



N, M = map(int, input().split())

land = [list(map(int, input().split())) for _ in range(N) ]
visited = [[0]*M for _ in range(N)]
ls_cnt = []
how_many_island(land)

count_bridge = max(land)
min_val = 99999
