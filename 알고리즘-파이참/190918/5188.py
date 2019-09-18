import sys
sys.stdin = open('5188.txt', 'r')
#
# def move(i, j):
#     if i and j == n-1:
#         return
#     else:
#         dx = [1, 0]
#         dy = [0, 1]
#         for k in range(2):
#             if i + dx[k] < n and j + dy[k] < n:
#                 return summ(i + dx[k], j + dx[k])

def summ(i, j, summm):
    global min_sum
    if i == n-1 and j == n-1:
        summm += matrix[i][j]
        if min_sum > summm:
            min_sum = summm

    elif summm < min_sum:
        summm += matrix[i][j]
        a_sum = summm
        dx = [1, 0]
        dy = [0, 1]
        for k in range(2):
            if i + dx[k] < n and j + dy[k] < n:
                summ(i + dx[k], j+ dy[k], a_sum)



for tc in range(1, int(input())+1):
    n = int(input()) # n X n 행렬
    matrix = [ list(map(int, input().split())) for _ in range(n)]
    stack = []
    min_sum = 999999
    summ(0, 0, 0)
    print('#%d %d' %(tc, min_sum))

