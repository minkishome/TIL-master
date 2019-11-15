import sys
sys.stdin = open('줄기세포.txt', 'r')

def iswall(x, y): # 안 써도 될 듯
    return 0 <= x < N and 0 <= y < M

def divide_cell():

tc = int(input())
for tn in range(1,tc+1):
    N, M, K = map(int, input().split()) # K시간 이후에 남아 있는 비활성, 활성세포만 (죽은거 제외)
    cell = [list(map(int, input().split())) for _ in range(N)]
    dir = [(1,0), (-1,0), (0,1), (0,-1)]
    for i in range(N):
        for j in range(M):

