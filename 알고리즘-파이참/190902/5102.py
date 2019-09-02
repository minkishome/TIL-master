import sys
sys.stdin = open('5102.txt', 'r')

from collections import deque

# test_num = int(input())
# for tc in range(test_num):
#     N, M = map(int, input().split())
#     ls = [0] * (2 * M)
#     for i in range(M):
#         ls[i*2], ls[2*i+1] = map(int, input().split())
#     start, end = map(int, input().split())
#     node_dict = {ls[i] : [] for i in range(len(ls))}
#
#     for i in range(M):
#         node_dict[ls[2*i]] += [ls[2 * i + 1]]
#         node_dict[ls[2 * i + 1]] += [ls[2*i]]
#     print(node_dict)
#     ls_check = deque([])
#
#     count = 0
#     que = deque([])
#     que.append(node_dict[start])
#     ls_check.append(start)
#     print(que)
#     while que:
#         ls_plus = deque([])
#         if end in ls_check:
#             break
#         count += 1
#         a = que.pop()
#
#         for i in a:
#             if i not in ls_check:
#                 ls_check.append(i)
#                 for j in node_dict[i]:
#                     ls_plus.append(j)
#         que.append(ls_plus)
#         print(que)
#         print(ls_check)
#     print('#%d %d' %(tc+1, count))

test_num = int(input())
for tc in range(test_num):
    N, M = map(int, input().split())
    ls = [ list(map(int, input().split())) for _ in range(M) ]

    start, end = map(int, input().split())
    q = []
    visitd = [0]*(N+1)
    q.append(start)
    while q:
        a = q.pop(0)
        for i in range(len(ls)):
            if ls[i][0] == a and not visitd[ls[i][1]]:
                q.append(ls[i][1])
                visitd[ls[i][1]] += visitd[a] + 1
                if ls[i][1] == end:
                    break
            if ls[i][1] == a and not visitd[ls[i][0]]:
                q.append(ls[i][0])
                visitd[ls[i][0]] += visitd[a] + 1
                if ls[i][0] == end:
                    break

    print('#%d %d' %(tc+1, visitd[end]))




# test_num = int(input())
# for tc in range(test_num):
#     N, M = map(int, input().split())
#     ls = [0] * (2 * M)
#     for i in range(M):
#         a, b = map(int, input().split())
#         ls[2 * i] = (a, b)
#         ls[2*i+1] = (b, a)
#
#     start, end = map(int, input().split())
#     ls_check = []
#     ls_plus = []
#     que = []
#     for i in ls:
#         if i[0] == start:
#             que.append(i[1])
#     ls_check.append(start)
#     count = 1
#     while 1:
#         if end in ls_check:
#             break
#         ls_plus = []
#         count += 1
#         for j in ls:
#             for i in que:
#                 if j[0] == i:
#                     if j[1] not in ls_check:
#                         ls_check.append(j[1])
#                         ls_plus.append(j[1])
#         que = ls_plus
#
#     print('#%d %d' %(tc+1, count))