import sys
sys.stdin = open('계단.txt', 'r')

def find_dis(a, b): # 여기서 a는 사람들 b는 stair
    return abs(a[0]-b[1]) + abs(a[1] - b[2]) #

def count_time(ls_to_st1, ls_to_st2, st): # st1:1번 계단 갈 놈 st2 : 2번 계단 갈 놈 st : 계단
    global min_val
    stair1 = []
    stair2 = []
    for i in ls_to_st1:
        time_1 = find_dis(i, st[0])
        stair1.append(time_1)
    for j in ls_to_st2:
        time_2 = find_dis(j, st[1])
        stair2.append(time_2) # 각자 걸리는 시간 구함
    # print(stair1, stair2)
    check_time1, check_time2 = 0, 0

    if stair2:
        stair2.sort()
        checked2 = [0] * len(stair2)
        wating_num2 = st[1][0]
        input_index = 0
        check_index = 0
        check_man = 0
        w_idx = 0
        # print(checked2)
        while 1:
            # print(check_index)
            check_time2 += 1
            for i in range(w_idx, len(stair2)):
                if stair2[i] < check_time2:
                    if checked2[i] == 0:
                        if check_man < 3:
                            if input_index < len(checked2):
                                # print(input_index)
                                checked2[input_index] = wating_num2
                                input_index += 1
                                check_man += 1
                                w_idx += 1
                            # print(checked2, check_man)

            for k in range(len(checked2)):
                if checked2[k] > 0:
                    checked2[k] -= 1
                    if checked2[k] == 0:
                        check_man -= 1
                        check_index += 1
            if check_man < 0:
                check_man = 0
            if check_index == len(stair2):
                break

    if stair1:
        stair1.sort()
        checked1 = [0] * len(stair1)  # 하나씩 넣을놈
        wating_num1 = st[0][0]
        input_index = 0
        check_index = 0
        check_man = 0
        w_idx = 0
        while 1:
            check_time1 += 1
            for i in range(w_idx, len(stair1)):
                if stair1[i] < check_time1:
                    if checked1[i] == 0:
                        if check_man < 3:
                            if input_index < len(checked1):
                                checked1[input_index] = wating_num1
                                input_index += 1
                                check_man += 1
                                w_idx += 1

            for k in range(len(checked1)):
                if checked1[k] > 0:
                    checked1[k] -= 1
                    if checked1[k] == 0:
                        check_man -= 1
                        check_index += 1
                        # print(checked1, check_man)
            if check_man < 0:
                check_man = 0
            if check_index == len(stair1):
                break
    res = max(check_time1, check_time2)
    if min_val > res:
        min_val = res








tc = int(input())
for tn in range(1, tc+1):
    N = int(input()) # 배열 가로, 세로
    arr = [list(map(int, input().split())) for _ in range(N)]
    people = []
    stair = []
    for x in range(N):
        for y in range(N):
            if arr[x][y] == 1:
                people.append([x,y])
            elif arr[x][y] != 0 and arr[x][y] != 1:
                stair.append([arr[x][y], x, y])
    # print(people, stair)
    # 계단과 사람을 모두 받아 옴
    min_val = 9999999
    power_set = [[]]
    for i in people:
        tmp = [[i] + p for p in power_set]
        power_set += tmp

    for i in range(0,2 ** (len(people))):
        count_time(power_set[i], power_set[-1-i], stair)
    print('#%d %d' %(tn, min_val+1))