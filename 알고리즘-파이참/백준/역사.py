n, m = map(int, input().split())
visited = [ [0]*(n) for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    visited[a-1][b-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if visited[i][k] and visited[k][j]:
                visited[i][j] = 1

s = int(input())
for _ in range(s):
    num1, num2 = map(int, input().split())
    if visited[num1-1][num2-1] == 1:
        print(-1)
    elif visited[num2-1][num1-1] == 1:
        print(1)
    elif visited[num1-1][num2-1] == 0:
        print(0)

        