import sys
sys.stdin = open('5207.txt', 'r')

def binary(ls, i, z, left_a, right_a):
    global cnt

    n = len(ls)
    l = left_a
    r = right_a
    if l > r:
        return
    mid = (l+r)//2

    if i == ls[mid]:
        cnt += 1
        return
    # left = ls[:mid]
    # right = ls[mid+1:]


    if i > ls[mid]:
        if z != 1:
            binary(ls, i, 1, mid+1, right_a)
    elif i < ls[mid]:
        if z != 2:
            binary(ls, i, 2, left_a, mid-1)





for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    ls_N = list(map(int, input().split()))
    ls_N.sort()
    ls_M = list(map(int, input().split()))
    cnt = 0
    for i in ls_M:
        if i in ls_N:
            binary(ls_N, i, 0, 0, len(ls_N)-1)
    print('#%d %d' %(tc, cnt))


