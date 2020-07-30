from itertools import permutations, combinations


# N, M, K = map(int, input().split())
#
#
#
# dp = [[(-1) for i in range(M+1)] for ii in range(N+1)]
# print(dp)
# def getDP(n, m):
#     if n==0 or m==0:
#         return 1
#     if dp[n][m] != -1:
#         return dp[n][m]
#
#     dp[n][m] = getDP(n-1, m) + getDP(n, m-1)
#     return dp[n][m]
#
# def func(n, m, k): #n은 a m은 z
#     ret = ""
#     print(ret)
#     print(getDP(n,m))
#     if n==0:
#         ret += 'z'*m
#         return ret
#     if m==0:
#         ret += 'a'*n
#         return ret
#
#     if getDP(n-1, m) > k:
#         print(ret)
#         ret += 'a'
#         ret += func(n-1,m,k)
#
#         return ret
#     else:
#         print(ret)
#         ret += 'z'
#         ret += func(n, m-1, k-getDP(n-1, m))
#         return ret
#
# if K > getDP(N, M):
#     print(-1)
# else:
#     print(func(N,M,K-1))
#
# for k in dp:
#     print(k)

n, m, k = map( int, input().split())

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

def getDP(n, m):
    if n==0 or m==0:
        return 1
    if dp[n][m] != 0:
        return dp[n][m]

    dp[n][m] = getDP(n-1, m) + getDP(n, m-1)
    return dp[n][m]

def func(n, m, k):
    res = ''
    if n == 0:
        res += 'z'*m
        return res
    if m == 0:
        res += 'a'*n
        return res
    if getDP(n-1, m) > k:
        res += 'a'
        res += func(n-1,m,k)
        return res
    else:
        res += 'z'
        res += func(n, m-1, k-getDP(n-1, m))
        return res

if k > getDP(n, m):
    print(-1)
else:
    print(func(n,m,k-1))

for k in dp:
    print(k)


