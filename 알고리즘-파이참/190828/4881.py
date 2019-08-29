# import sys
# sys.stdin = open('4881.txt','r')
#
#
# def sum_ls(i,k,N,ls_sum):
#     global min_value, arr, visited
#     if k == N:
#         if ls_sum < min_value:
#             min_value = ls_sum
#     else:
#         k += 1# 다음 행으로 가야하니깐
#         ls_part = ispromising()
#         for c in ls_part:
#             visited[c] = True
#             if ls_sum + arr[i][c] < min_value: # 가지치는 조건
#                 sum_ls(i+1, k, N, ls_sum + arr[i][c])
#             visited[c] = False
#
# def ispromising():
#     global min_value, arr, visited
#     ls_part = []
#     for n in range(N): # False인 경우에 값을 더할 것이기에
#         if not visited[n]:
#             ls_part.append(n)
#     return ls_part
#
#
# for t in range(int(input())):
#     N = int(input())
#     visited = [False] * N
#     arr = [list(map(int, input().split())) for m in range(N)]
#     ls_idx = [0] * N # 이걸 통해 겹치지 않게 덧셈을 해줄 것
#     k = 0
#     min_value = 1000
#     ls_sum = 0 # 각 순서에 따른 합
#     i = 0
#     sum_ls(i,k,N,ls_sum)
#     print('#%d %d'%(t+1, min_value))

mir = {0:1, 1:2, 3:4, 2:5}
a = 1
print(a)
a = mir[a]
print(a)