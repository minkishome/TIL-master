import sys
sys.stdin = open('기지국.txt', 'r')

def find_home(ls, i, j, N):
    a,b = i,j # 값을 계속 돌려야하니깐
    loca = {'A' : 4, 'B' : 8, 'C' : 12}
    num = loca[ls[i][j]]
    dx = [1, -1, 0, 0, 2,-2, 0, 0, 3, -3 ,0 ,0]
    dy = [0, 0, 1, -1, 0, 0, 2, -2, 0, 0, 3,-3] # 나누지 말고 딕셔너리 이용해서 바로 값을 불러오면 될듯
    if ls[i][j] == 'A': # 1번
        for z in range(num):
            i = a
            j = b
            i += dx[z]
            j += dy[z]
            if 0 <= i <=N and 0 <= j <= N:
                if ls[i][j] == 'H':
                    ls[i][j] = 'X'


test_num = int(input())
for tc in range(test_num):
    N = int(input())
    ls = list(input().split())
    for i in range(N):
        for j in range(N):
            if ls[i][j] != 'H' or 'X':
                find_home((ls,i, j, N)
    print(ls)
