import sys
sys.stdin = open('등산로.txt', 'r')

def iswall(x, y): return 0 <= x < N and 0 <= y < M

def make_load(cnt, que):
    global max_val
    if not que:
        if max_val < cnt:
            max_val = cnt
            return
    else:
        while que:
            n = que.pop()
            kx = n[0]
            ky = n[1]
            for dxdy in dxdys:
                nx = kx + dxdy[0]
                ny = ky + dxdy[1]
                if iswall(nx, ny) and san[nx][ny] < san[kx][ky]:
                    que.append([nx, ny])

tc = int(input())
for tn in range(1,tc+1):
    N, K = map(int,input().split())
    san = [list(map(int, input().split())) for _ in range(N)]
    max_height = max(san)
    ls_max = []
    for x in range(N):
        for y in range(N):
            if san[x][y] == max_height:
                ls_max.append([x,y])
    # 가장 높은 지점 찾음
    max_val = 0
    dxdys = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for xy in ls_max:
        kx = xy[0]
        ky = xy[1]
        que = []
        for dxdy in dxdys:
            nx = kx + dxdy[0]
            ny = ky + dxdy[1]
            if iswall(nx, ny) and san[nx][ny] < san[kx][ky]:
                que.append([nx, ny])



