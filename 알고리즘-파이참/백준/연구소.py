from itertools import combinations # 3개 조합짜서 그거 max값을 구함
from collections import deque
import copy
def iswall(x,y):
    return 0<=x<n and 0<=y<m

def spread(ls):
    global max_value
    stack = deque([])
    for vi in virus:
        stack.append(vi)
        while stack:
            x,y = stack.popleft()
            for dx,dy in dxdy:
                nx, ny = x+dx, y+dy
                if iswall(nx,ny) and ls[nx][ny] == 0:
                    ls[nx][ny] = 2
                    stack.append((nx,ny))
    sum_space = 0
    for kk in ls:
        sum_space += kk.count(0)
    # print(sum_space, 21312312)
    if sum_space > max_value:
        max_value = sum_space
    return
n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

dxdy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
space = []
virus = []
max_value = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            virus.append((i,j))
        elif arr[i][j] == 0:
            space.append((i,j))
# print(virus)
# print(space)
# for k in combinations(space,3):
#     print(k)
for step in combinations(space, 3):
    arr2 = copy.deepcopy(arr)
    for q,w in step:
        arr2[q][w] = 1
    spread(arr2)
print(max_value)