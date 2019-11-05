def iswall(x,y): return 0 <= x < n and 0 <= y < n
def isrange(n,m): return l <= abs(n-m) <= r
# 범위를 초기에 함수로 지정


n, l, r = map(int, input().split())
arr = [list(map(int, input().split()))  for _ in range(n)]


direction = [(1,0), (-1,0), (0,1), (0,-1)]
cnt = 0
while True:
    flag = False
    visited = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if not visited[x][y]:
                path = []
                tmp_sum = 0
                queue = [(x, y)]
                while queue:
                    tmp = []
                    for kx, ky in queue:
                        if not visited[kx][ky]:
                            visited[kx][ky] = 1
                            tmp_sum += arr[kx][ky]
                            path.append((kx, ky))
                            for (dx, dy) in direction:
                                new_x, new_y = kx+dx, ky+dy
                                if iswall(new_x, new_y) and not visited[new_x][new_y]:
                                    if isrange(arr[new_x][new_y], arr[kx][ky]):
                                    # 조건에 새로운 점들이 부합하는지
                                        tmp.append((new_x, new_y))
                    queue = tmp
                path_len = len(path)
                path_cnt = tmp_sum//path_len
                for px, py in path:
                    arr[px][py] = path_cnt
                if path_len > 1:
                    flag = True
    if flag:
        cnt += 1
    else:
        break
print(cnt)
