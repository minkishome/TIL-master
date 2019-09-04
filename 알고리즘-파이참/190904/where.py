import sys
sys.stdin = open('where.txt', 'r')

# def find(maze, k):
#     global N, M
#     dx = [1, 0]
#     dy = [0, 1]
#     a = 0
#     for i in range(N):     # -dx -dy로 한번 더 검색을 해서 진행 반대방향으로도 해당이 되는지 확인해야한다.
#         for j in range(N):
#             if maze[i][j] == 1:
#                 count = 0
#                 for k in range(4):
#
#                     x = i + dx[k]
#                     y = j + dy[k]
#                     x2 = i - dx[k]
#                     y2 = j - dy[k]
#                     if 0 <= x < N and 0 <= y < N:
#                         if maze[x][y] == 1:
#                             count += 1
#                             # if 0 <= x2 < N and 0 <= y2 < N:
#                             #     if maze[x2][y2] == 1:
#                             #         continue
#                             while maze[x][y] != 1:
#                                 if maze[x][y] == 1:
#                                     count += 1
#                                     x = x + dx[k]
#                                     y = y + dy[k]
#
#
#                 if count == k:
#                     a += 1
#                     # print(i, j)
#                 count = 0
#     return a
# for tc in range(int(input())):
#     N, M = map(int, input().split())
#     puzzle = [ list(map(int, input().split())) for _ in range(N)]
#     print('#%d %d' %(tc+1, find(puzzle, M)))
for tc in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for x in range(n):
        for y in range(n):
            if arr[x][y] == 1:
                if y == 0 or y > 0 and arr[x][y - 1] == 0:
                    d = 0
                    while 0 <= y + d < n and arr[x][y + d] == 1:
                        d += 1
                    if d == k:
                        cnt += 1

            if arr[y][x] == 1:
                if y == 0 or y > 0 and arr[y - 1][x] == 0:
                    d = 0
                    while 0 <= y + d < n and arr[y + d][x] == 1:
                        d += 1
                    if d == k:
                        cnt += 1
    print('#%d %d' % (tc, cnt))