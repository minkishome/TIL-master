# from collections import deque
#
#
# def move(_x, _y, _dx, _dy, _c):
#     while arr[_x+_dx][_y+_dy] != '#' and arr[_x][_y] != 'O':
#         _x += _dx
#         _y += _dy
#         _c += 1
#     return _x, _y, _c
#
#
#
# def bfs():
#     while q:
#         rx, ry, bx, by, d = q.popleft()
#         if d > 10:
#             break
#         for dx,dy in dxdy:
#             # print(dx,dy)
#             nrx,nry,rc = move(rx,ry,dx,dy,0)
#             nbx,nby,bc = move(bx,by,dx,dy,0)
#             # print(arr[nrx][nry])
#             if arr[nbx][nby] == '0':
#                 continue
#             if arr[nrx][nry] == 'O':
#                 # print('come')
#                 return d+1
#             if nrx == nbx and nry == nby:
#                 if rc > bc:
#                     nrx, nry = nrx-dx, nry-dy
#                 else:
#                     nbx, nby = nbx - dx, nby - dy
#
#             if not visited_red[nrx][nry] or not visited_blue[nbx][nby]:
#
#                 visited_red[nrx][nry] = 1
#                 visited_blue[nbx][nby] = 1
#                 q.append((nrx,nry,nbx,nby,d+1))
#
#
#     return -1
#
#
# # 그냥 한쪽부터  시작하면 된다.
# N, M = map(int,input().split())
# arr = [list(input()) for _ in range(N)]
#
# ball = []
# final = []
# visited_red = [[0]*M for _ in range(N)]
# visited_blue = [[0]*M for _ in range(N)]
#
# dxdy = [(0,1), (1,0), (0,-1), (-1,0)]
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 'R':
#             rx, ry = i, j
#             visited_red[rx][ry] = 1
#         if arr[i][j] == 'B':
#             bx, by = i, j
#             visited_blue[bx][by] = 1
# # 구슬의 위치를 넣어 주고
# q = deque([[rx, ry, bx, by, 0]])
# cnt = bfs()
# print(cnt)

N, M = map(int, input().split())
B = [list(input()) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = []
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
def pos_init():
    rx, ry, bx, by = 0, 0, 0, 0  # 초기화
    for i in range(N):
        for j in range(M):
            if B[i][j] == 'R':
                rx, ry = i, j
            elif B[i][j] == 'B':
                bx, by = i, j
    # 위치 정보와 depth(breadth 끝나면 +1)
    queue.append((rx, ry, bx, by, 1))
    visited[rx][ry][bx][by] = True

def move(x, y, dx, dy):
    cnt = 0  # 이동 칸 수
    # 다음이 벽이거나 현재가 구멍일 때까지
    while B[x+dx][y+dy] != '#' and B[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def solve():
    pos_init()  # 시작 조건
    while queue:  # BFS : queue 기준
        rx, ry, bx, by, depth = queue.pop(0)
        if depth > 10:  # 실패 조건
            break
        for i in range(4):  # 4방향 이동 시도
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])  # Red
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])  # Blue
            if B[nbx][nby] != 'O':  # 실패 조건이 아니면
                if B[nrx][nry] == 'O':  # 성공 조건
                    print(depth)
                    return
                if nrx == nbx and nry == nby:  # 겹쳤을 때
                    if rcnt > bcnt:  # 이동거리가 많은 것을
                        nrx -= dx[i]  # 한 칸 뒤로
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                # breadth 탐색 후, 탐사 여부 체크
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    # 다음 depth의 breadth 탐색 위한 queue
                    queue.append((nrx, nry, nbx, nby, depth+1))
    print(-1)  # 실패 시

solve()
