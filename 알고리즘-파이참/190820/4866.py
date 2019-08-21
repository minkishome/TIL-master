import sys

sys.stdin = open('4866.txt', 'r')

ts = int(input())

for test_num in range(1,ts+1):
    string = list(input())
    ls_idx = [0] * len(string)  # 괄호의 인덱스에 숫자를 입력
    result = 0          # 내가 찾는 결과값
    for i in range(len(string)):
        if string[i] == '(':
            ls_idx[i] = 1
        if string[i] == ')':
            ls_idx[i] = 2
        if string[i] == '{':
            ls_idx[i] = 3
        if string[i] == '}':
            ls_idx[i] = 4


    while 0 in ls_idx:
        ls_idx.remove(0)

    if len(ls_idx) % 2 != 0:
        result = 100


    z = 0  # 강제 종료
    while 1:
        for i in range(len(ls_idx) - 1):
            if ls_idx[i] == ls_idx[i + 1] -1:
                del ls_idx[i]
                del ls_idx[i]
                break
        z += 1
        if z == 50:
            break

    if ls_idx == []:
        result = 0
    if result == 0:
        print('#%d 1' % (test_num))
    else:
        print('#%d 0' % (test_num))


    #
    #     for i in range(len(ls_idx)-2, 2):
    #         if ls_idx[i] == ls_idx[i+1]:
    #             result += 0
    #         else:
    #             result += 1




