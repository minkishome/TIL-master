from itertools import combinations

def iswall(x, y):
    return 0 <= x < N and 0 <= y < N


N, M = map(int, input().split())
town = [ list(map(int,input().split())) for _ in range(N) ]
chicken = []
house = []
for i in range(N):
    for j in range(N):
        if town[i][j] == 2:
            chicken.append((i,j))
        elif town[i][j] == 1:
            house.append((i,j))
dxdy = [(1,0), (-1,0), (0,1), (0,-1)]

minmin_dis = 100000
for sele in combinations(chicken,M):

    dis = 0
    for a in house: 
        min_dis = 1000
        for k in sele:
            dis2 = abs(a[0]-k[0])+abs(a[1]-k[1])

            if min_dis > dis2:
                min_dis = dis2
                
        dis += min_dis
    if minmin_dis > dis:
        minmin_dis = dis
print(minmin_dis)
        