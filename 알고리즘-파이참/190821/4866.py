def find_gate(ls):
    new_ls = []
    for i in ls: # 받는게 없는 경우를 생각하지 않음;;
        if i =='(':
            new_ls.append('(')
        elif i == '{':
            new_ls.append('{')
        elif i == '}':
            if new_ls[-1] != '{':
                return 0
            else:
                new_ls.pop(-1)
        elif i == ')':
            if new_ls[-1] != '(':
                return 0
            else:
                new_ls.pop(-1)

    if new_ls == []:
        return 1

import sys
sys.stdin = open('4866.txt', 'r')

test_num = int(input())

for tc in range(test_num):
    string = list(input())
    a = find_gate(string)
    print('#%d %d' %(tc+1,a))
