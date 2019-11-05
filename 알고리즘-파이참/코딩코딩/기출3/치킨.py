import itertools

n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
houses= []
chickens = []

for x in range(n):
    for y in range(n):
        if maze[x][y]:
            if maze[x][y] == 1:
                houses.append((x,y))
            else:
                chickens.append((x,y))
c_len = len(chickens)
h_len = len(houses)
dist = [[0]*len(houses) for _ in range(c_len)]
for c_idx, (cx, cy) in enumerate(chickens):
    for h_idx, (hx, hy) in enumerate(houses):
        dist[c_idx][h_idx] = abs(cx-hx) + abs(cy-hy)

store_options = set(range(c_len))
# [[2, 2, 2, 5, 6, 6], [6, 2, 4, 3, 4, 4], [7, 3, 5, 4, 5, 3],
# [6, 4, 4, 3, 4, 2], [5, 7, 5, 2, 1, 1]]
print(store_options)
print(dist)

min_cnt = 9999999999
for option in itertools.combinations(store_options, m):
    cnt = 0
    for j in range(h_len):
        tmp = 99999
        for i in option:
            if dist[i][j] < tmp:
                tmp = dist[i][j]
        cnt += tmp
        if cnt > min_cnt:
            break

    if cnt < min_cnt:
        min_cnt = cnt

print(min_cnt)