import sys
sys.stdin = open('화물.txt', 'r')

#
# def find(ls,z):
#     global n
#     if z == n:
#         return len(ls2)
#
#     for i in range(num - 1):
#         if ls[i] != 0:
#             min_idx = i
#             for j in range(i+1, num):
#                 if ls[j] != 0 and ls[min_idx] != 0:
#                     if ls[min_idx][1] > ls[j][1]:
#                         min_idx = j
#                     if ls[min_idx][0] >= ls2[-1][1]:
#                         ls2.append(ls[min_idx])
#                         ls[min_idx] = 0
#                         find(ls, z+1)
#
#
#
#
# for tc in range(1, int(input())+1):
#     n = int(input())
#     ls = [list(map(int, input().split())) for _ in range(n)]
#     check = [False] * (n+1)
#     a = ls[0]
#     for i in range(len(ls)):
#         if ls[i][1] < a[1]:
#             a = ls[i]
#             b = i
#     print(ls)
#     ls2 = [a]
#     num = len(ls)
#     check[b] = True
#     ls[b] = 0
#
#     num2 = find(ls,0)
#     print(num2)
#     print(ls2)
#     # print('#%d %d' %(tc, len(ls2) +1 ))



#     for i in range(num - 1):
#         if ls[i] != 0:
#             min_idx = i
#             for j in range(i+1, num):
#                 if ls[j] != 0 and ls[min_idx] != 0:
#                     if ls[min_idx][1] > ls[j][1]:
#                         min_idx = j
#                     if ls[min_idx][0] >= ls2[-1][1]:
#                         ls2.append(ls[min_idx])
#                         ls[min_idx] = 0
#                         find(ls, z+1)
#

T = int(input())
for tc in range(T):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if data[j][1] < data[min][1]:
                min = j
            elif data[j][1] == data[min][1]:
                if data[j][0] > data[min][0]:
                    min = j
        data[i], data[min] = data[min], data[i]
    visited = [0] * 24
    total = 0
    for ii in range(n):
        if sum(visited[data[ii][0]:data[ii][1]]) == 0:
            for jj in range(data[ii][0], data[ii][1]):
                visited[jj] = 1
            total += 1
    print("#{} {}".format(tc + 1, total))