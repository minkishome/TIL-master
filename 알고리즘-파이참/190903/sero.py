import sys
sys.stdin = open('sero.txt', 'r')

for tc in range(int(input())):
    ls = [ list(map(str, input())) for _ in range(5)]
    max = len(ls[0])
    for i in ls:
        if max < len(i):
            max = len(i)
    for i in ls:
        if len(i) < max:
            for j in range(max-len(i)):
                i.append(' ')
    ls1 = []
    for i in range(max):
        for j in range(5):
            if ls[j][i] != ' ':
                ls1.append(ls[j][i])
    a = ''.join(ls1)
    print('#%d %s' %(tc+1, a))