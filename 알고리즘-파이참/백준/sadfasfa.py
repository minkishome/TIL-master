from collections import deque

def iswall(x, y, n):
    return 0 <= x < n and 0 <= y < n

def solution(board):
    answer = 0
    n = len(board)
    dxdy = [(0,1), (1,0), (-1,0), (0,-1)]
    visited = [[0]*len(board) for _ in range(len(board))]
    stack = deque()
    if board[0][1] == 0:
        visited[0][1] = [100, (0, 0)]
        stack.append((0,1))
    if board[1][0] == 0:
        visited[1][0] = [100, (0, 0)]
        stack.append((1,0))
    while stack:
        dq = stack.popleft()
        for dx, dy in dxdy:
            new_x, new_y = dq[0] + dx, dq[1] + dy
            if iswall(new_x, new_y, n):
                if board[new_x][new_y] != 1:
                    if visited[new_x][new_y] == 0:
                        if new_x != visited[dq[0]][dq[1]][1][0] and new_y != visited[dq[0]][dq[1]][1][1]:
                            visited[new_x][new_y] = [visited[dq[0]][dq[1]][0] + 600, (dq[0], dq[1])] # 90도로 꺾을 때
                            stack.append((new_x, new_y))
                        else:
                            visited[new_x][new_y] = [visited[dq[0]][dq[1]][0] + 100, (dq[0], dq[1])]
                            stack.append((new_x, new_y))
                    else: # 값이 있을 떄
                        if new_x != visited[dq[0]][dq[1]][1][0] and new_y != visited[dq[0]][dq[1]][1][1]:
                            price = visited[dq[0]][dq[1]][0] + 600
                            if visited[new_x][new_y][0] > price:
                                visited[new_x][new_y] = [price, (dq[0], dq[1])]
                                stack.append((new_x, new_y))
                        else:
                            # print(dq[0], dq[1])
                            price = visited[dq[0]][dq[1]][0] + 100
                            if visited[new_x][new_y][0] > price:
                                visited[new_x][new_y] = [price, (dq[0], dq[1])]
                                stack.append((new_x, new_y))
    answer = visited[n-1][n-1][0]
    # for k in visited:
    #     print(k)
    return answer

board = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]
print(solution(board))
