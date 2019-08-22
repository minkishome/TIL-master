def find_gate(ls):
    new_ls = []
    for i in ls:
        if i =='(':
            new_ls.append('(')
        elif i == '{':
            new_ls.append('{')
        elif i == '}':
            if new_ls[-1] != '{':
                return 1
            else:
                new_ls.pop(-1)
        elif i == ')':
            if new_ls[-1] != '(':
                return 1
            else:
                new_ls.pop(-1)

    if new_ls == []:
        return 2

import sys
sys.stdin = open('4866.txt', 'r')

test_num = int(input())
for tc in range(test_num):
    string = list(input())
    a = int(find_gate(string))
    print('#%d %d' %(tc+1, a-1))
