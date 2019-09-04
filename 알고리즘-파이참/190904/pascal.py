import sys
sys.stdin = open('pascal.txt', 'r')

def pascal(a):
    if a == 1:
        ls = [1]
        return ls
    if a == 2:
        ls = [1, 1]
        return ls
    else:
        ls = pascal(a-1)
        ls2 = [0] * len(ls)
        for i in range(len(ls)-1):
            ls2[i] = ls[i] + ls[i+1]
        new_ls = [0] * a
        new_ls[0], new_ls[-1] = 1, 1
        for i in range(1,len(new_ls)-1):
            new_ls[i] = ls2[i-1]
        return new_ls



for tc in range(int(input())):
    N = int(input())
    print('#%d' % (tc + 1))
    for j in range(1,N+1):
        ls = pascal(j)

        for i in range(len(ls)):
            print(ls[i] ,end = ' ')
        print()

