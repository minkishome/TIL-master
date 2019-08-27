import sys, copy
sys.stdin = open('magnetic.txt', 'r')


for num in range(1, 11):
    tc = int(input())
    plain = [[0] for _ in range(tc)]
    for i in range(tc):
        plain[i] = list(map(int, input().split()))
    count = 0

    for k in range(100):
        stack = []
        for l in range(100):
            if plain[l][k] == 1:
                stack += [1]
            if plain[l][k] == 2:
                if stack:
                    count += 1
                    stack = []



    print('#%d %d' %(num, count))
