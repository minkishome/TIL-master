import sys
from itertools import permutations
sys.stdin = open('숫자만들기.txt', 'r')



def make_number(res, depth, list_cal):
    global beta, max_val, min_val
    if depth == beta-1: # 여기 고치자

        if max_val < res:
            max_val = res
        if min_val > res:
            min_val = res
    else:

        for i in range(4):
            if i == 0 and list_cal[i] != 0:
                copy_list = list_cal[:]
                new_res = res + ls_num[depth+1]
                copy_list[i] = list_cal[i] - 1
                make_number(new_res, depth+1, copy_list)
            elif i == 1 and list_cal[i] != 0:
                copy_list = list_cal[:]
                new_res = res - ls_num[depth+1]
                copy_list[i] = list_cal[i] - 1
                make_number(new_res, depth+1, copy_list)
            elif i == 2 and list_cal[i] != 0:
                copy_list = list_cal[:]
                new_res = res * ls_num[depth+1]
                copy_list[i] = list_cal[i] - 1
                make_number(new_res, depth+1, copy_list)
            elif i == 3 and list_cal[i] != 0:
                copy_list = list_cal[:]
                if res < 0:
                    new_res = int((-1)*res // ls_num[depth+1])
                    new_res *= -1
                else:
                    new_res = int(res // ls_num[depth + 1])
                copy_list[i] = list_cal[i] - 1
                make_number(new_res, depth+1, copy_list)



tc = int(input())
for tn in range(1, tc+1):
    N = int(input())
    ls_count2 = list(map(int, input().split())) # + - * /

    # print(ls_count)


    ls_num = list(map(int, input().split())) # 수식에 사용되는 숫자
    beta = len(ls_num)


    max_val = -999999
    min_val = 999999
    make_number(ls_num[0],0,ls_count2)
    # for z in lslsls:
    #     calculate(z)
        # print(z)
    # print(max_val, min_val)
    print('#%d %d'%(tn, (max_val-min_val)))


