import sys

sys.stdin = open('4866.txt', 'r')

ts = int(input())

for test_num in range(1,ts+1):
    string = list(input())
    ls_idx = [0]*len(string)
    result = 0
    for i in range(len(string)):
        if string[i] == '(':
            ls_idx[i] = 1
        if string[i] == ')':
            ls_idx[i] = 1
        if string[i] == '{':
            ls_idx[i] = 2
        if string[i] == '}':
            ls_idx[i] = 2
    while not 0 in ls_idx:
        ls_idx.remove(0)
    if len(ls_idx)%2 != 0:
        result = 100
    j = 0
    while j < 10:
                        
    #
    #     for i in range(len(ls_idx)-2, 2):
    #         if ls_idx[i] == ls_idx[i+1]:
    #             result += 0
    #         else:
    #             result += 1
    # if result == 0:
    #     print('#%d 1' %(test_num))
    # else:
    #     print('#%d 0' % (test_num))



