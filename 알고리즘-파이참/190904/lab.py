import sys
sys.stdin = open('lab.txt', 'r')

def find_way(ls, a, b, idx):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        





N, M = map(int, input().split())

ls_lab = [ list(map(int, input().split())) for _ in range(M) ]
count_2 = 0
for i in range(M):
    count_2 += ls_lab[i].count(2)
ls_where2 = []
ls_way = [[0] * count_2 ] # 각각의 좌표를 찾기위해
loca = 0
for i in range(N):
    for j in range(M):
        if ls_lab[i][j] == 2:
            ls_where2.append([i,j])
            loca += 1
