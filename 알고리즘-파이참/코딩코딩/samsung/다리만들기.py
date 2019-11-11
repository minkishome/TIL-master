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


def make_dari(depth, cnt, land_ls):
    global min_val, tmp_sum
    if depth == count_bridge: # 완전탐색해서 모두 연결 되어있는지
        if len(land_ls) == ls_cnt:
            if min_val > cnt:
                min_val = cnt
                return
    else:
        for k in ls_cnt:# ls_cnt는 섬의 번호 모은 리스트
            for x in range(N):
                for y in range(M):
                    if land[x][y] == k:
                        for alpha in dxdys:
                            nx, ny = x, y
                            tmp = 0
                            while 1:
                                nx += alpha[0]
                                ny += alpha[1]
                                if iswall(nx, ny) and not land[nx][ny]:
                                    tmp += 1
                                    if land[nx][ny] != k and land[nx][ny] != 0 and land[nx][ny] not in land_bridge and tmp != 1:
                                        if k not in land_bridge:
                                            land_bridge.append(k)
                                        land_bridge.append(land[nx][ny])
                                        tmp_sum += tmp # 다리 최소값
                                        break
                                else:
                                    break








N, M = map(int, input().split())
dxdys = [(1, 0), (0, 1), (-1, 0), (0, -1)]
land = [list(map(int, input().split())) for _ in range(N) ]
visited = [[0]*M for _ in range(N)]
ls_cnt = []
how_many_island(land)
land_bridge = [] # 다리만들어진 섬의 갯수
count_bridge = max(land)
min_val = 99999
tmp_sum = 0
