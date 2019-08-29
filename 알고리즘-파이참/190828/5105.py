import sys
sys.stdin = open('input_10_100.txt', 'r')


def ispromising(r, c, maze):
    global count, short
    if maze[r][c] == 0:
        count += 1
        maze[r][c] = 1
        return 1
    elif maze[r][c] == 1:
        count += 1
        pass
    elif maze[r][c] == 2:
        count += 1
        return 2


def solve_maze(ls, a, b, N): # 리스트와 시작점과 마지막 점

    if ispromising() == 3:
        pass
    else:
        if count < short:
            for i in dx:
                for j in dy:
                    x = alpha[0] + i
                    y = alpha[1] + j
                    if x >= 0 and x <= N - 1 and y >= 0 and y <= N - 1:
                        solve_maze(ls,x,y,N)


    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visit = {(a,b)}
    while visit:
        alpha = visit.pop()

        for i in dx:
            for j in dy:
                x = alpha[0] + i
                y = alpha[1] + j
                if x >= 0 and x <= N-1 and y >= 0 and y <= N-1:
                    if ls[x][y] == '3':
                        return 1
                    if ls[x][y] == '0':
                        if (x,y) not in visit:
                            ls[x][y] = 1
                            visit.add((x, y))
        if len(visit) == 0 :
            return 0





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