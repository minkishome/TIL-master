import sys
sys.stdin = open('lab.txt', 'r')

def find(ls, a, b, ls2):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if ls[x][y] == 0:
            ls[a][b] == 1
            ls2.append([x,y])



N, M = map(int, input().split())

ls = [list(map(int, input().split())) for _ in range(M)]
print(ls)
count = 0
for i in range(N):
    for j in range(M):
        if ls[i][j] == 2:
            count += 1
