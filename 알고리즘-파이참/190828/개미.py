def move(matrix, i,j, k, N): # 리스트, 좌표 ij, k는 dx,dy를 나타낼 것 count는 횟수
    global count
    dx = [1, 0, -1, 0] # x가 행
    dy = [0, 1, 0, -1] # y가 열
    i += dx[k]
    j += dy[k]
    count += 1
    mir1 = {0:3, 1:2, 2:1, 3:0}
    mir2 = {0:1, 1:0, 2:3, 3:2}
    if not 0 <= i <= N-1 or not 0 <= j <= N-1:
        return count-1
    if matrix[i][j] == 0:
        return move(matrix, i, j, k, N)
    if matrix[i][j] == 1: # 1번 거울을 만났을때
        k = mir1[k]
        return move(matrix, i, j, k, N)
    if matrix[i][j] == 2: # 2번 거울을 만났을때
        k = mir2[k]
        return move(matrix, i, j, k, N)
import sys
sys.stdin = open('개미.txt', 'r')

test_num = int(input())
for tc in range(test_num):
    count = 0
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    print(move(matrix, 0, 0, 1, N))
