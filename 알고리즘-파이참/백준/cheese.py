import sys
sys.stdin = open('cheese.txt', 'r')
sys.setrecursionlimit(100000)

def find(ls, n, k, c): # k는 0,1이 아닌 숫자, n 은 현재 몇번째인지? c는 1의 갯수
    global N, M
    num1, num2 = 0, 0
    for i in range(N):
        for j in range(M):
            if ls[i][j] == n:
                num1 = i
                num2 = j
                break
    print(num1, num2)
    stack = []
    que = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    for z in range(4):
        x = num1 + dx[z]
        y = num2 + dy[z]
        if 0 <= x < N and 0 <= y < M:
            if ls[x][y] == n and [x, y] not in stack:
                stack.append([x, y])
                que.append([x, y])
                while que: # 가장 밖ㅇ ㅔ있는 1과 붙은 0ㅇ을 찾는다.
                    plain = que.pop()
                    ls[plain[0]][plain[1]] = k
                    for z in range(4):
                        x = plain[0] + dx[z]
                        y = plain[1] + dy[z]
                        if 0 <= x < N and 0 <= y < M:
                            if ls[x][y] == n and [x, y] not in stack: # n = 0
                                stack.append([x, y])
                                que.append([x, y])
                    print(stack)
    for i in stack:
        ls[i[0]][i[1]] = k



    # for i in range(N):
    #     for j in range(M):
    #         if ls[i][j] == k:
    #             for z in range(4):
    #                 x1 = i + dx[z]
    #                 y1 = j + dy[z]
    #                 if 0 <= x1 < N and 0 <= y1 < M:
    #                     if ls[x1][y1] == n + 1:
    #                         ls[x1][y1] = k



    a = 0
    for num in ls:
        a += num.count(1)
    if a == 0:
        return k
    else:
        find(ls, k, k+1, a)




N, M = map(int, input().split())

cheese = [ list(map(int, input().split())) for _ in range(N)]

print(find(cheese, 0, 3, 0))