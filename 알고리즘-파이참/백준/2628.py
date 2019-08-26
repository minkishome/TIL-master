import sys, copy
sys.stdin = open('2628.txt', 'r')

# a = tuple(map(int, input().split()))
#
# tc = int(input())
# garo_sero = [[1]*a[0] for _ in range(a[1])] # 좌표값
# slicing = [[0] for _ in range(tc)]
# garo = []
# sero = []
# for test in range(tc):
#     slicing[test] = list(map(int,input().split()))
#
#
#
# for i in range(len(slicing)-1):
#     if slicing[i][0] == 0:# 가로에 대한 정렬
#         min_idx = i
#         for j in range(i+1,len(slicing)):
#             if slicing[j][0] == 0:
#                 if slicing[min_idx][1] > slicing[j][1]:
#                     min_idx = j
#                 if min_idx != i:
#                     slicing[i] , slicing[min_idx] = slicing[min_idx], slicing[i]
#
# for u in range(len(slicing) - 1):
#     if slicing[u][0] == 1:  # 세로에 대한 정렬
#         min_idx = u
#         for k in range(u + 1, len(slicing)):
#             if slicing[k][0] == 1:
#                 if slicing[min_idx][1] > slicing[k][1]:
#                     min_idx = k
#                 if min_idx != u:
#                     slicing[u], slicing[min_idx] = slicing[min_idx], slicing[u]
#
# for i in slicing:
#     if i[0] == 0:
#         garo.append(i[1])
#
# for j in slicing:
#     if j[0] == 1:
#         sero.append(i[1])
# plain = []
# for i in garo:
#     for j in sero:
#         plain.append([i,j])
# print(plain)
#
# # garo와 sero의 위치에 따른 정렬
#
# list_part = [] # 나눠지는 리스트들을 저장할 곳
#
# for i in range(len(plain)):
#     if i == 0:
#
#     else:
#         pass
#
#
#
# # for i in range(tc):
# #     if slicing[i][0] == 0:
# #         list_part[i] = copy.deepcopy(garo_sero[:slicing[i][1]])
# #         for j in range(slicing[i][1]):
# #             for k in range(a[0]):
# #                 garo_sero[j][k] = 0
# # 세로에 대한 변경
#
#
#
# print(garo_sero)
# print(list_part)

h,w = map(int,input().split())
c = int(input())
wp = [0]
hp = [0]
max_w = 0
max_h = 0
for _ in range(c):
    data = input().split()
    if data[0] =='0':
        wp.append(int(data[1]))
    else:
        hp.append(int(data[1]))

wp.sort()
wp.append(w)
hp.sort()
hp.append(h)
print(wp, hp)
for i in range(len(wp)-1):
    if max_w < wp[i+1] - wp[i]:
        max_w = wp[i+1] - wp[i]
for i in range(len(hp) - 1):
    if max_h < hp[i+1] -hp[i]:
        max_h = hp[i+1] -hp[i]
print(max_w*max_h)