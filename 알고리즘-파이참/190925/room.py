import sys
sys.stdin = open('room.txt', 'r')

def gostop(i, j, cnt, original_i, original_j):
    global max_cnt, min_xy
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]
    for k in range(4):
        new_i = i + dx[k]
        new_j = j + dy[k]
        if 0 <= new_i < N and 0 <= new_j < N:
            if maze[i][j] +1 == maze[new_i][new_j]:
                gostop(new_i, new_j, cnt+1, original_i, original_j)
                break
    if max_cnt <= cnt:
        if max_cnt < cnt:
            max_cnt = cnt
            min_xy = maze[original_i][original_j]
        else:
            if min_xy > maze[original_i][original_j]:
                min_xy = maze[original_i][original_j]


for tc in range(1, int(input())+1):
    N = int(input())
    maze = [ list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0
    min_xy = 99999999
    for i in range(N):
        for j in range(N):
            gostop(i,j,1,i,j)
    print('#%d %d %d' %(tc, min_xy, max_cnt))