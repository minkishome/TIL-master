import sys
sys.stdin = open('5177.txt', 'r')


def traversal(N):
    if N < 1:
        return

    if tree[N] < tree[N//2]:
        tree[N], tree[N//2] = tree[N//2], tree[N]
    # if n >= 2*N +1:
    #     if tree[N] > tree[2*N +1]:
    #         tree[N], tree[2*N + 1] = tree[2*N+1], tree[N]
        traversal(N//2)




for tc in range(1, int(input())+1):
    n = int(input())
    ls = list(map(int, input().split()))
    tree = [0]
    for i in range(n):
        tree.append(ls[i])
        traversal(i+1)
    # print(tree)

    summ = 0
    while n > 1:
        n //= 2
        summ += tree[n]

    print('#%d %d' %(tc, summ))