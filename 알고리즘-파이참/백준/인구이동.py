import copy
from collections import deque as dq

def iswall(x,y):
    return 0 <= x < N and 0 <= y < N

def make_avr(people, cnt):
    ls_copy = copy.deepcopy(people) 
    stack = dq()
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                population = []
                stack.append((i,j))
                population.append((i,j))
                visited[i][j] = 1
                while stack:
                    point = stack.popleft()
                    x , y = point[0], point[1]
                    for dx, dy in dxdy:
                        if iswall(x+dx, y+dy) and not visited[x+dx][y+dy]:
                            minus = abs(people[x][y] - people[x+dx][y+dy])
                            if L <= minus and minus <= R:
                                stack.append((x+dx,y+dy))
                                population.append((x+dx,y+dy))
                                visited[x+dx][y+dy] = 1
                if len(population) > 1:
                    summ = 0
                    for k in population:
                        summ += people[k[0]][k[1]]
                    summ = int(summ / len(population))
                    for k in population:
                        people[k[0]][k[1]] = summ
    # print(people)
    # print(ls_copy)
    # print(cnt)
    if people == ls_copy:
        return cnt
    else:
        cnt += 1
        return make_avr(people, cnt)
    




N, L, R = map(int,input().split())# 인구 L < x < R
peo = [list(map(int,input().split())) for _ in range(N)]

dxdy = [(1,0), (0,1), (-1,0), (0,-1)]
# cnt = 0

a = make_avr(peo, 0)

print(a)

