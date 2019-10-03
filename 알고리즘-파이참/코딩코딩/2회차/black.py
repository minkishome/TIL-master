# def find(z, summ):
#     global max_val
#     if z == 3:
#         if summ <= M and summ > max_val:
#             max_val = summ
#
#     else:
#         for i in range(N):
#             if not check[i]:
#                 check[i] = True
#                 new_summ = summ + card_ls[i]
#                 if new_summ <= M:
#                     find(z+1, new_summ)
#                     check[i] = False

import itertools



N, M = map(int, input().split())
card_ls = list(map(int, input().split()))

black_jack = itertools.combinations(card_ls, 3)

max_val = 0
for i in black_jack:
    if sum(i) <= M and max_val < sum(i):
        max_val = sum(i)

print(max_val)