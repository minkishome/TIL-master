from copy import deepcopy
def solution(m, n, board, cnt):
    answer = 0
    arr = []
    dxdy = [(0,0), (1,0), (0,1), (1,1)] # 4개만 보면 된다.
    if type(board[0]) != list:
        for k in board:
            arr.append(list(k))
    else:
        arr = deepcopy(board)

    stack = []
    for i in range(m-1):
        for j in range(n-1):
            if arr[i][j] != 0:
                if arr[i][j] == arr[i+1][j] ==arr[i][j+1] == arr[i+1][j+1]:
                    for k in range(4):
                        x, y = i + dxdy[k][0], j + dxdy[k][1]
                        if (x, y) not in stack:
                            stack.append((x,y))
                            # arr[x][y] = 0
    cnt += len(stack)
    for x, y in stack:
        arr[x][y] = 0

    for i in range(m-2, -1, -1):
        for j in range(n):
            if arr[i][j] and arr[i+1][j] == 0:
                for k in range(m-i):
                    if arr[i+k][j]:
                        arr[i][j], arr[i+k-1][j] = arr[i+k-1][j], arr[i][j]

    if stack:
        return solution(m, n, arr, cnt)
    else:
        cnt = answer
        print(cnt)
        return answer



solution(4, 5, 	['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ'],0)