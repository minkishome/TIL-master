import sys
sys. stdin = open('4875.txt', 'r')

def find(): # 재귀로 다시 한번 원하는 결과값이 나올때 까지 반복하는 구조로 while없이도 가능함
    


#
# def solve_maze(ls, a, b, N): # 리스트와 시작점과 마지막 점
#     dx = [1,-1,0,0]
#     dy = [0,0,1,-1]
#     visit = {(a,b)}
#     while visit:
#         alpha = visit.pop()
#
#         for i in dx:
#             for j in dy:
#                 x = alpha[0] + i
#                 y = alpha[1] + j
#                 if x >= 0 and x <= N-1 and y >= 0 and y <= N-1:
#                     if ls[x][y] == '3':
#                         return 1
#                     if ls[x][y] == '0':
#                         if (x,y) not in visit:
#                             ls[x][y] = 1
#                             visit.add((x, y))
#         if len(visit) == 0 :
#             return 0





test_num = int(input())
for num in range(1,test_num+1):
    N = int(input())
    maze = [0] * N
    for c in range(N):
        ls = list(input())
        maze[c] = ls

    start = {}
    for i in range(N):
        for j in range(N):
            if int(maze[i][j]) == 2:
                start = (i,j)


    print('#%d %d ' %(num, solve_maze(maze, start[0], start[1], N)))