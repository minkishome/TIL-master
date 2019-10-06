# def make_line(m, lsls):
#     if m == M:
#         for i in range(M-1):
#             if lsls[i] < lsls[i+1]:
#                 print(''.join(lsls))
#
#
#     else:
#         for i in range(1,N+1):
#             if not check[i]:
#                 check[i] = True
#                 lsls.append(i)
#                 make_line(m+1, lsls)
#                 lsls.pop(-1)
#                 check[i] = False
#
#
#
# N, M = map(int,input().split())
# ls = [0] * (N+1)
# for i in range(1,N+1):
#     ls[i] = i
# check = [False] * (N+2)
# ls2 = []
# make_line(0,ls2)


ls = []
print(sum(ls))