import sys
sys.stdin = open('장훈이.txt', 'r')

def find(summ, k):
    global min_sum
    for i in range(k, N):
        new_summ = summ + ls[i]
        if new_summ < min_sum:
            if B <= new_summ:
                min_sum = new_summ
            else:
                find(new_summ, i+1)


for tc in range(1, int(input()) + 1):
    N, B = map(int, input().split())
    ls = list(map(int, input().split()))
    min_sum = 999999
    find(0,0)
    print('#%d %d' %(tc, min_sum-B))


# def backtracking(k_sum, idx):
#     global minsum
#     if idx == n and b <= k_sum:
#         minsum = k_sum
#     else:
#         for x in range(idx, n):
#             temp = k_sum + arr[x]
#             if temp < minsum:
#                 if b <= temp:
#                     minsum = temp
#                 else:
#                     backtracking(temp, x + 1)
#
#
# for tc in range(1, int(input()) + 1):
#     n, b = map(int, input().split())
#     arr = list(map(int, input().split()))
#     minsum = 999999
#     backtracking(0, 0)
#     print('#%d %d' % (tc, minsum - b))