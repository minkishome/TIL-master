import sys, math
sys.stdin = open('swim.txt', 'r')



#

for tc in range(1, int(input())+1):
    ls_price = list(map(int, input().split()))
    go_swim = list(map(int, input().split()))
    ls_check = [0, 0, 0, 0]
#     max_val = ls_price[3]
#     a = 0
#     for i in go_swim:
#         if i != 0:
#             a += 1
#     new_price = (a//3)*go_swim[2] + (a%3)*go_swim[1]
#





    #
    # a = math.ceil(ls_price[1]/ls_price[0])
    # b = math.ceil(ls_price[2]/ls_price[1])
    # c = math.ceil(ls_price[3]/ls_price[2])
    #
    #
    # for i in go_swim:
    #     if i < a:
    #         ls_check[0] += i
    #     elif i >= a:
    #         ls_check[1] += 1
    #
    #         # ls_check[1] = ls_check[1]%3
    #     elif ls_check[1] >= b:
    #         ls_check[2] += ls_check[1]//3
    #         ls_check[1] = ls_check[1]%3
    #     elif ls_check[2] >= c:
    #         ls_check[3] = 1
    #         ls_check[2] = 0
    #         ls_check[1] = 0
    #         ls_check[0] = 0
    # price = 0
    # for j in range(4):
    #     price += ls_price[j] * ls_check[j]
    # print(tc, price)
    # print(ls_check)