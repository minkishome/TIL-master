from collections import deque


def move(_x, _y, _dx, _dy, _c):
    while arr[_x+_dx][_y+_dy] != '#' and arr[_x][_y] != 'O':
        _x += _dx
        _y += _dy
        _c += 1
    return _x, _y, _c



def bfs():
    while q:
        rx, ry, bx, by, d = q.popleft()
        if d > 10:
            break
        for dx,dy in dxdy:
            # print(dx,dy)
            nrx,nry,rc = move(rx,ry,dx,dy,0)
            nbx,nby,bc = move(bx,by,dx,dy,0)
            # print(arr[nrx][nry])
            if arr[nbx][nby] == '0':
                continue
            if arr[nrx][nry] == 'O':
                # print('come')
                return d+1
            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx, nry = nrx-dx, nry-dy
                else:
                    nbx, nby = nbx - dx, nby - dy

            if not visited_red[nrx][nry] or not visited_blue[nbx][nby]:

                visited_red[nrx][nry] = 1
                visited_blue[nbx][nby] = 1
                q.append((nrx,nry,nbx,nby,d+1))


    return -1


# 그냥 한쪽부터  시작하면 된다.
N, M = map(int,input().split())
arr = [list(input()) for _ in range(N)]

ball = []
final = []
visited_red = [[0]*M for _ in range(N)]
visited_blue = [[0]*M for _ in range(N)]

dxdy = [(0,1), (1,0), (0,-1), (-1,0)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            rx, ry = i, j
            visited_red[rx][ry] = 1
        if arr[i][j] == 'B':
            bx, by = i, j
            visited_blue[bx][by] = 1
# 구슬의 위치를 넣어 주고
q = deque([[rx, ry, bx, by, 0]])
cnt = bfs()
print(cnt)
