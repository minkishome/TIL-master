# n = int(input())
#
# list_num = list(map(int, input().split()))
#
# dp = [[0]*n for _ in range(n)]
#
# for i in range(n):
#     dp[0][i] = list_num[i]
#
#
# for i in range(0, n-1):
#     dp[1][i] = list_num[i] + list_num[i+1]
#
# for i in range(2, n):
#     for j in range(0, n-i+1):
#         dp[i][j] = dp[i-1][j] + dp[i-1][j+1] - dp[i-2][j+1]
#
# ans = 0
# for k in dp:
#     ex = max(k)
#     if ans < ex:
#         ans = ex
#
#
#
# print(ans)

n = int(input())
num_list = list(map(int, input().split()))
temp = [0 for _ in range(n)]


result = -1001

for i in range(n):
    temp[i] = max(temp[i - 1] + num_list[i], num_list[i])
    result = max(result, temp[i])

print(result)