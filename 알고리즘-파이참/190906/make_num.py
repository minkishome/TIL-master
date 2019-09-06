import sys
import copy
sys.stdin = open('make_num.txt', 'r')
import time

def move(x, y, k, strin):
    global num_list, maze
    if k == 7:
        num_list.add(strin)
    else:
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < 4 and 0 <= new_y < 4:
                new_strin = strin + maze[new_x][new_y]
                move(new_x, new_y, k+1, new_strin)

for tc in range(int(input())):
    maze = [list(map(str, input().split())) for _ in range(4)]
    num_list = set() # 생성된 숫자들을 append
    for i in range(4):
        num_str = str() # 붙인 숫자들을 이어줄 스트링
        for j in range(4):
            k = 0  # 카운트 후 7이 될 경우 출력
              # 숫자를 뺄 때마다 0으로 바뀌기에 하나를 복사해놓는다.
            move(i, j, k, num_str)
    print(num_list)
    print('#%d %d' %(tc+1, len(num_list)))

# def move(x, y, k, strin):
#     global num_list, maze
#     k += 1
#     dx = [1, -1, 0, 0]
#     dy = [0, 0, 1, -1]
#     que = []
#     for i in range(4):
#         new_x = x + dx[i]
#         new_y = y + dy[i]
#         if 0 <= new_x < 4 and 0 <= new_y < 4:
#             que.append([new_x, new_y])
#     while que:
#         a = que.pop()
#         new_strin = strin + maze[a[0]][a[1]]
#         # if ls[a[0]][a[1]] != '0':
#         #     ls2[a[0]][a[1]] = '0'
#         # print(ls, ls2, new_x, new_y, k)
#         if k == 7:
#             if new_strin not in num_list:
#                 num_list.append(new_strin)
#                 #print(new_strin)
#             return
#         else:
#             move(a[0], a[1], k, new_strin)
#
#
#
#
#
# for tc in range(int(input())):
#     maze = [list(map(str, input().split())) for _ in range(4)]
#     num_list = [] # 생성된 숫자들을 append
#     for i in range(4):
#         num_str = str() # 붙인 숫자들을 이어줄 스트링
#         for j in range(4):
#             k = 0  # 카운트 후 7이 될 경우 출력
#               # 숫자를 뺄 때마다 0으로 바뀌기에 하나를 복사해놓는다.
#             move(i, j, k, num_str)
#
#     print('#%d %d' %(tc+1, len(num_list)))

