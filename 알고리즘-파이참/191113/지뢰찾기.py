import sys
sys.stdin = open('지뢰찾기.txt', 'r')

import copy

def iswall(x,y):
    return 0 <= x < N and 0 <= y < N

def find_boom(ls_boom, cnt):
    stack_change_num = []
    stack_put_if_num = []
    ls_copy_boom = copy.deepcopy(ls_boom)
    for i in range(N):
        for j in range(N):
            if boom[i][j] == '.':
                for k in dir:
                    cnt_boom = 0
                    dx, dy = i + k[0], j + k[1]
                    if boom[dx][dy] == '*' and iswall(dx, dy):
                        cnt_boom += 1
                if not cnt_boom:
                    stack_change_num.append((i, j))
                    while stack_change_num:
                        alpha = stack_change_num.pop()
                        for k in dir:
                            dx, dy = alpha[0] + k[0], alpha[1] + k[1]
                            cnt_boom2 = 0
                            if iswall(dx, dy):
                                for u in dir:
                                    nx, ny = dx + u[0], dy + u[1]
                                    if boom[nx][ny] =='*' and iswall(nx, ny):
                                        cnt_boom2 += 1
                                ls_copy_boom[dx][dy] = cnt_boom2
                                if cnt_boom2 == 0:
                                    stack_change_num.append((dx, dy))


                                 ### 전체 while문 돌리는거 생각




tc = int(input())
for tn in range(1, tc+1):
    N = int(input())
    boom = [list(map(int,input().split())) for _ in range(N)]
    # 0이면 연속적으로 보임, 주변에 *이 있으면 그에 따라 숫자가 1씩 증가
    # stack이 두개 있어야 한다. 하나는 주변 숫자를 바꿀 수 있는 리스트 (무조건 0)
    # 하나는 다른 리스트에서 주변
    boom_number = copy.deepcopy(boom)
    dir = [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,-1),(-1,1),(-1,0)]