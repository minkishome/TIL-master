import sys

sys.stdin = open('4615.txt', 'r')

def change(ls, i, j, N):
    if ls[i][j] == 1:

    else:




for tc in range(int(input())):
    N, M = map(int, input().split())
    ls = [ [0]*N for _ in range(N)]
    print(ls)
    count = 1
    # x로 1,2 -1,-2 했을때 그 값이 각각 나와 다르고 같을때 중간애를 바꿔준다 y도 같음

    while count < M:
        count += 1
        ls1 = map(int, input().split())
        ls[ls1[0]][ls1[1]] = ls1[2]
