import sys
sys.stdin = open('2001.txt', 'r')

for _ in range(int(input())):
    N, M = map(int, input().split())
    ls = [list(map(int, input().split())) for _ in range(N)]
    max_value = 0
    cursum = 0
    for i in range(N-M+1):
        for j in range(N-M+1): # 시작점
            for z in range(i,i+M):
                for u in range(j, j+M):
                    cursum += ls[z][u]
            if max_value < cursum:
                max_value = cursum
            cursum = 0
    print(max_value)