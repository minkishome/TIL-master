import sys
sys.stdin = open('계산기.txt')


def rhkfgh(idx_num,ls_input ,ls_output, plus):
    global count
    if ls_input[i] in ls:
        if ls_input[i] == '+':
            plus.append('+')
        if ls_input[i] == '*':
            plus.append('*')

    elif ls_input[i] in ls1:
        if ls_input[i] == '(':
            return rhkfgh()
        if ls_input[i] == ')':
            return i


# 기본적으로 플러스는 안에 쌓아두고 나중에 뽑는다. 곱하기는 그와 다르게 만나고 숫자하나 더 넣은 다음에 바로 넣고
ls = ['+','*']
ls1 = ['(']  #, ')']
ls_back = []
ls_plus = []

for _ in range(10):
    count = 0
    n = int(input())
    ls_all = list(input())
    print(ls_all)
    i = 0
    while 1:
        a = ls_all[i]
        if a in ls:
            if a == '+':

            else:

            pass
        elif a in ls1:
            rhkfgh(i, ls_all, ls_back, plus)
        else: # 숫자에 대해
            ls_back.append(a)
            if ls_plus[-1] == '*':
                ls_back.append(ls_plus[-1])



        if i == len(ls_all):
            break
        i += 1


    # for i in ls_all:
    #     if i in ls: # 기본적인 연산자에 대한 과정
    #         if i == '+':
    #
    #         else:
    #         pass
    #     elif i in ls1: # 괄호를 만났을때 경우 괄호를 먼저 다 해결?
    #         while 1:
    #             if i in
    #
    #             if i == ')':
    #                 break
    #         pass
    #     else: # int
