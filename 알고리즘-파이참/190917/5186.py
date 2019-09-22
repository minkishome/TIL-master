import sys, math
sys.stdin = open('5186.txt', 'r')


def convert_2(num, i, string):
    if i == 13:
        string = 'overflow'
        return string
    if num > 2**(-i):
        num = num - 2**(-i)
        print(num, end = ' ')
        string += '1'
    else:
        string += '0'
    if math.isclose(num, 0): # 근접한 값으로 변경
        return string
    else:
        return convert_2(num, i+1, string)


for tc in range(1, int(input())+1):
    n = float(input())
    string = str()
    asdf = convert_2(n, 1, string)

    print('#%d %s' %(tc, convert_2(n, 1, string)))
