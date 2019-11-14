import sys
sys.stdin = open('벽돌.txt', 'r')

from collections import deque
import copy

def iswall(x,y):
    return 0 <= x < H and 0 <= y < W

# 굳이 cnt가 있을 필요 없다.
def break_block(depth, x,y, list1_2,): # 주어진거 받고나서 그걸 깰때 또 주변을 깨는지 아닌지를 확인 들어온건 카피해주고 깬건 다시 그대로 넣어줘야한다!!
    global dxdys
    stack = deque()
    stack.append([x,y, list1_2[x][y]])
    list1_2[x][y] = 0
    while stack:
        # print(stack)
        a = stack.popleft()
        # if list1_2[a[0]][a[1]]: # 중복되는 점 제거
        n = a[2]
        # list1_2[a[0]][a[1]] = 0 # 원래 점 2으로 만든다.
        for z in range(1, n):
            for k in dxdys:
                dx, dy  = a[0] + z*k[0], a[1] + z*k[1]
                # print(dx, dy)
                if iswall(dx, dy) and list1_2[dx][dy]:
                    stack.append((dx,dy,list1_2[dx][dy]))
                    list1_2[dx][dy] = 0

    block_1or2 = [[0] * W for _ in range(H)]
    for j in range(W-1, -1, -1):
        b = H -1
        for i in range(H-1, -1, -1):
            if list1_2[i][j] != 0:
                block_1or2[b][j] = list1_2[i][j]
                b -= 1
    ## 다 해주고 나면 한 점에 있어서 벽돌을 모두 깨는 경우 완성
    # # 끝나고 나면 다시 찾는 거로 재귀
    # print()
    # print(depth)
    # print(*block_1or2, sep='\n')
    return find_way(depth+1, block_1or2)




def find_way(depth, list_1_2): # list_block은 얼마까지 깰 수 있는지, list_1_2는 벽돌이 있는지 없는지를 list_block 필요없을듯?
    global min_val
    val2 = 0
    for z in list_1_2:
        val2 += z.count(0)
    val = W * H - val2
    if val < min_val:
        min_val = val

    if depth == N:
        return
    else:
                # i = 0
        # while i < H:
        #     for j in range(W):
        #         if list_1_2[i][j] == 0:
        #             continue
        #         else:
        #             break_block(depth,i, j, new_list_1_2)
        #     i += 1
        for j in range(W):
            new_list_1_2 = copy.deepcopy(list_1_2)

            for i in range(H):
                if list_1_2[i][j] != 0:
                    break_block(depth, i, j, new_list_1_2)
                    break





tc = int(input())
for tn in range(1, tc+1):
    N, W, H = map(int, input().split())
    block = [list(map(int, input().split())) for _ in range(H)]
    # block_1or2 = [ [0]*W for _ in range(H)]

    # for x in range(H):
    #     for y in range(W):
    #         if block[x][y] == 0:
    #             block_1or2[x][y] = 0
    #         else:
    #             block_1or2[x][y] = 1

    dxdys = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    min_val = 9999
    find_way(0, block)
    print('#%d %d' %(tn, min_val))