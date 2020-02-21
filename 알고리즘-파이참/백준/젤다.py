from collections import deque

def iswall(x, y):
    return 0 <= x < n and 0 <= y< n

def move(i, j, loopy):
    global min_loopy
    if i == n -1 and j == n - 1:
        visited[n-1][n-1] = 0
        # loopy += arr[n-1][n-1]
        if loopy < min_loopy:
            min_loopy = loopy
    else:
        # stack = deque()
        # stack.append((i, j))
        # while q
        for k in range(4):
            nx, ny = i + dxdy[k][0], j + dxdy[k][1]
            if iswall(nx, ny) and not visited[nx][ny]:
                new_loopy = loopy + arr[nx][ny]
                if min_loopy < new_loopy:
                    continue
                else:
                    visited[nx][ny] = 1
                    move(nx, ny, new_loopy)
                    visited[nx][ny] = 0


cnt = 1
while 1:
    n = int(input())

    if n == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(n)]
    min_loopy = 99999
    visited = [[0]*n for _ in range(n)]
    dxdy = [(1,0), (0,1), (-1,0), (0,-1)]
    visited[0][0] = 1
    move(0, 0, arr[0][0])
    print('Problem %d: %d' %(cnt, min_loopy))
    cnt += 1