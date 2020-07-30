from collections import deque as dq

def iswall(x, y):
    return 0 <= x < n and 0 <= y < n



n, l, r = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
dxdy = [(0,1), (1,0), (-1,0), (0,-1)]
cnt = 0

while 1:
    flag = 0
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                que = dq([(i, j)])
                stack = [(i, j)]
                visited[i][j] = 1
                summ = arr[i][j]
                while que:
                    qq = que.popleft()
                    for dx ,dy in dxdy:
                        x, y = qq[0] + dx, qq[1] + dy
                        if iswall(x, y) and not visited[x][y]:
                            if l <= abs(arr[qq[0]][qq[1]] - arr[x][y]) <= r:
                                que.append((x,y))
                                stack.append((x, y))
                                visited[x][y] = 1
                                summ += arr[x][y]
                                flag = 1

                # 다 넣었을때
                if flag:
                    avg = summ//len(stack)
                    for k in stack:
                        arr[k[0]][k[1]] = avg
    if flag == 1:
        cnt += 1

    if flag == 0:
        break
print(cnt)
