# def solution(numbers, hand):
#     answer = ''
#     arr = [(3,1),
#            (0,0), (0,1), (0,2),
#            (1,0), (1,1), (1,2),
#            (2,0), (2,1), (2,2),
#            (3,0),  (3,2)
#            ]
#     lefty = [1, 4, 7]
#     righty = [3, 6, 9]
#     left_num, right_num = 10, 12
#     for k in numbers:
#         if k in lefty:
#             answer += 'L'
#             left_num = k
#         elif k in righty:
#             answer += 'R'
#             right_num = k
#         else: # 숫자가 중간에 있을 때
#             min_right = abs(arr[k][0]-arr[right_num][0]) +abs(arr[k][1]-arr[right_num][1])
#             min_left = abs(arr[k][0]-arr[left_num][0]) + abs(arr[k][1]-arr[left_num][1])
#             if min_left > min_right:
#                 answer += 'R'
#                 right_num = k
#             elif min_left < min_right:
#                 answer += 'L'
#                 left_num = k
#             else:
#                 if hand == "right":
#                     answer += 'R'
#                     right_num = k
#                 else:
#                     answer += 'L'
#                     left_num = k
#
#     return answer
#
#

####################################

from itertools import permutations
from copy import deepcopy
def solution(expression):
    answer = 0
    num = ''
    ls_numm = []
    ls_dustkss = []
    dustkswk = ['+', '-', '*']
    for k in expression:
        if k not in dustkswk:
            num += k
        else:
            ls_numm.append(int(num))
            num = ''
            ls_dustkss.append(k)
    ls_numm.append(int(num))
    max_val = 0
    for dustks in permutations(dustkswk):
        ls_num = deepcopy(ls_numm)
        ls_dustks = deepcopy(ls_dustkss)
        for char in dustks:
            idx = 0
            for idxx in ls_dustks:
                if idxx == char:
                    if idxx == '+':
                        ls_num[idx] = ls_num[idx] + ls_num[idx + 1]

                    elif idxx == '-':
                        ls_num[idx] = ls_num[idx] - ls_num[idx + 1]

                    elif idxx == '*':
                        ls_num[idx] = ls_num[idx] * ls_num[idx + 1]

                    ls_num.pop(idx+1)
                    ls_dustks.pop(idx)
                    pass
                idx += 1
            # if len(ls_num) == 1:
            #     break
        if len(ls_num) == 1:
            val = abs(ls_num[0])
            if max_val < val:
                max_val = val
        else:
            k = ls_dustks[0]
            if k == '+':
                val = ls_num[0] + ls_num[1]
            elif k =='-':
                val = ls_num[0] - ls_num[1]
            elif k == '*':
                val = ls_num[0] * ls_num[1]
            if max_val < abs(val):
                max_val = abs(val)
        # print(ls_numm, ls_dustks)
    print(ls_num, ls_dustks)
    answer = max_val
    return answer

exp = "100-200*300-500+20"
print(solution(exp))