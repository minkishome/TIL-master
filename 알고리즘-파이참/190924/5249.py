import sys
sys.stdin = open('5249.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int,input().split())
    check = [0] * (N+1) # 모든 정점을 가는지 확인
    check[0] = 1
