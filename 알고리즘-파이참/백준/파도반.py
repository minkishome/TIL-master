from collections import deque

def iswall(x,y):
    return 0 <= x < n and 0 <= y < n

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [ [0]*n for _ in range(n)]

dxdy = [(1,0), (0,1), (-1,0), (0,-1)]

cnt = 1
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0 and not visited[i][j]:
            q = deque()
            q.append((i, j))
            while q:
                x, y = q.popleft()
                arr[x][y] = cnt
                visited[x][y] = 1
                for k in range(4):
                    new_x, new_y = x + dxdy[k][0], y + dxdy[k][1]
                    if iswall(new_x, new_y) and arr[new_x][new_y] != 0 and not visited[new_x][new_y]:
                        q.append((new_x,new_y))
            cnt += 1


dist = [[0] for _ in range(cnt)]
visited = [ [0]*n for _ in range(n)]
for k in range(1, cnt):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == k:
                for d in dxdy:
                    new_x, new_y = i + d[0], j + d[1]
                    if iswall(new_x, new_y):
                        if arr[new_x][new_y] == 0 and not visited[i][j]:
                            dist[k].append((i,j))
                            visited[i][j] = 1
                            pass
min_value = 1000
cnt -= 1

for x in range(1, cnt):
    for y in range(x+1, cnt+1):
        for k in dist[x]:
            for l in dist[y]:
                if k != 0 and l != 0:
                    bridge = abs(k[0] - l[0]) + abs(k[1] - l[1]) -1
                    if min_value > bridge:
                        min_value = bridge

print(min_value)