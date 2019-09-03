import sys
sys.stdin = open('5105.txt', 'r')



def find(maze, a, b, count):
    global N # 범위 제한
 # 다시 돌아가는 방법 정해야함
      # 모든 방향이 0인지 확인
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]

        if 0 <= x < N and 0 <= y < N:
            if maze[x][y] == 3:
                return count

            if maze[x][y] == 1:
                continue
            if maze[x][y] == 0:
                maze[x][y] = 1
                count += 1
                return find(maze, x, y, count)
    else:
        return 0



test_num = int(input())
for tc in range(test_num):
    N = int(input())
    count = 0
    maze = [list(map(int, input())) for _ in range(N)]
    print(maze)
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                print(find(maze, i, j, 0))
