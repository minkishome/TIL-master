import sys
sys.stdin = open('4881.txt', 'r')
def isPromising(i, cursum):
    global minsum, visited
    res = [] # 부분 배열의 인덱스
    for n in range(N):
        if not visited[n]: # false인 경우에만 res에 더한다
            res.append(n) # 구해줄 배열 간 합
    return res
def findingSum(i, k, N, cursum):
    global arr, minsum # 전체 영역 변수
    if k == N: # k와 N이 같아진다면 마지막 행까지 모든 작업 수행
        if cursum < minsum:
            minsum = cursum # 최소값을 바꿔줌
    else:
        k += 1
        res = isPromising(i, cursum)
        for c in res:
            visited[c] = True
            if cursum + arr[i][c] < minsum:
                findingSum(i+1, k, N, cursum+arr[i][c])
            visited[c] = False
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for m in range(N)]
    visited = [False]*N # 향후 더할 배열에서 중복되지 않는 값을 만들기 위해
    print(arr)
    minsum = 91 # 미리 최대값을 넣음
    k = 0 # 몇번째 배열인지 정하기 위해
    cursum = 0 # 각 배열간 합을 구함
    i = 0
    findingSum(i,k,N,cursum)
    print(minsum)
# Collapse




