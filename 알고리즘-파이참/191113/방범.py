import sys
sys.stdin = open('방범.txt', 'r')

tc = int(input())
for tn in range(tc):
    N, M = map(int, input().split()) # N = 도시 크기,  M 은 한 집이 낼 수 있는 최대 비용
    city = [list(map(int, input().split())) for _ in range(N)]
    

    cost = k**2 + (k-1)**2 # k는 여기서 방범회사가 만드는 비용