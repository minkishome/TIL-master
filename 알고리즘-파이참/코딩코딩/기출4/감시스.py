# 1 : 1방향 2: 양방향 3: 90도 4 : 3방향 5 : 전체

def cctv(ls1, ls2):
    for k in ls2:
        if k[0] == 1:
            for z in range(4):

        if k[0] == 2:
            for z in range(2):
        if k[0] == 3:
            for z in range(4):
        if k[0] == 4:
            for z in range(4):

    pass





N, M = map(int, input().split())

office = [list(map(int, input().split())) for _ in range(N) ]
cctv_location = []
# cctv 위치를 받고 그걸 어떻게
for i in range(N):
    for j in range(M):
        if office[i][j] == 5:
            for k in range(N):
                if office[k][j] == 0:
                    office[k][j] = '#'
            for k in range(M):
                if office[i][k] == 0:
                    office[i][k] = '#'

        if office[i][j] and office[i][j] not in ['#', 6]:
            if office[i][j] != 5:
                cctv_location.append([office[i][j], i, j ])

change = [1, -1]

for z in office:
    print(z)
print(cctv_location)
min_val = 9999


