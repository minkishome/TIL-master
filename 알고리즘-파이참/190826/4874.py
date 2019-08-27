import sys
sys.stdin = open('4874.txt', 'r')

def find_ans(ls):
    stack = []
    ls2 = ['+', '*', '-', '/', '.']
    ls4 = ['+', '*', '-', '/']
    num1 = 0
    num2 = 0

    for i in ls:
        if i not in ls2:
            num1 += 1
        elif i in ls4:
            num2 += 1
    if num1 != num2 +1:
        return 'error'

    for j in ls:
        if j not in ls2:
            stack.append(int(j))
        elif j in ls4:
            if len(stack) <= 1:
                return 'error'
            else:
                a = int(stack.pop(-1))
                b = int(stack.pop(-1))
                if j == '+':
                    stack.append(a + b)
                elif j == '-':
                    stack.append(b - a)
                elif j == '*':
                    stack.append(a * b)
                elif j == '/':
                    stack.append(b / a)
        elif j == '.':
            return stack[0]






num = int(input())

for tc in range(1,num+1):
    ls_num = list(input().split())
    print('#%d %s' %(tc, find_ans(ls_num)))



