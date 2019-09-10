import sys
sys.stdin = open('5176.txt', 'r')



#
#
# for tc in range(int(input())):

# def traveresal(t):
#     global cnt
#     if numbers[t]:
#         traveresal(2 * t)
#         cnt += 1
#         tree[t] = cnt
#         traveresal(2 * t + 1)
#
#
#
# for tc in range(1, int(input()) + 1):
#     n = int(input())
#     numbers = [i for i in range(n + 1)] + [0] * (n + 1)
#     print(numbers)
#     tree = [0] * (n + 1)
#     cnt = 0
#     traveresal(1)
#     print('#%d %d %d' % (tc, tree[1], tree[n // 2]))

def traversel(N):
    global cnt
    if N > n:
        return
    traversel(2*N)
    cnt += 1
    tree[N] = cnt
    traversel(2*N + 1)



for tc in range(1, int(input()) + 1):
    n = int(input())
    ls_idx = [0] * (n+1)
    tree = [0] * (n+1)
    cnt = 0
    traversel(1)
    print('#%d %d %d' %(tc, tree[1], tree[n//2]))