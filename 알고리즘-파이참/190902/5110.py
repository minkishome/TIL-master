import sys
sys.stdin = open('5110.txt', 'r')

from collections import deque

test_num = int(input())
for tc in range(test_num):
    N, M = map(int, input().split())
    ls1 = deque(map(int, input().split()))
    for i in range(M-1):
        ls3 = deque([])
        ls2 = deque(map(int, input().split()))
        a = len(ls1)
        for j in range(len(ls1)):
            if ls1[j] > ls2[0]:
                for _ in range(len(ls1)-j):
                    ls3.append(ls1.pop())
                ls1.extend(ls2)
                ls1.extend(reversed(ls3))
                break

        if a == len(ls1):
            ls1.extend(ls2)
    ls1 = list(ls1)
    ls4 = ls1[len(ls1)-10:len(ls1)]
    # for _ in range(10):
    #     ls4.append(ls1.pop())
    print('#%d' %(tc+1) ,end = ' ')
    print(' '.join(map(str, reversed(ls4))))
