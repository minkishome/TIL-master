import sys
from collections import deque
sys.stdin = open('samsung_bus.txt', 'r')

test_num = int(input())

for tc in range(test_num):
    ls_count = [0]*5001
    N = int(input())
    for i in range(N):
        a, b = map(int,input().split())
        for j in range(a, b+1):
            ls_count[j] += 1

    P = int(input())
    print('#%d' %(tc+1) ,end = ' ')
    for i in range(P):
        c = int(input())
        print(ls_count[c], end = ' ')
    print()