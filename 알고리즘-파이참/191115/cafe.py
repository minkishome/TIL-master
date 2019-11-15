import sys
sys.stdin = open('cafe.txt', 'r')


def iswall(x,y):
    return 0 <= x < N and 0 <= y < N

def move(origin_x, origin_y, k, visit):# k는 방향


def count_cafe(i, j, ):
    cnt = 0
    visited = [0] * 101
    visited[i][j] = 1

tc = int(input())
for tn in range(1, tc+1):
    N = int(input())
    dessert = [list(map(int, input().split())) for _ in range(N)]
    dir = [(1,1), (1,-1), (-1,-1), (-1,1)] # 0번은 2번 제외 1번은 3번 제외 2번은 0번 제외 3번은 1번 제외 *(-1)만 아니면 된다. 그리고 사각형이 나와야함

    max_value = 0
    for i in range(N):
        for j in range(N)