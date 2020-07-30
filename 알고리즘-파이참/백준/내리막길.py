from copy import deepcopy
from collections import deque as dq

def iswall(x, y):
    return 0 <= x < n and 0 <= y < m

def find(i, j):
    global answer
    que = dq()
    que.append((i, j))
    print(que)
    while que:

        x, y = que.popleft()
        for dx, dy in dxdy:
            new_x, new_y = x + dx, y + dy
            if iswall(new_x, new_y):
                if arr[new_x][new_y] < arr[x][y]:
                    visited[new_x][new_y] += 1
                    que.append((new_x,new_y))


    return




n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dxdy = [(1,0), (0,1), (-1,0), (0,-1)]

answer = 0

find(0, 0)
print(visited[n-1][m-1])


