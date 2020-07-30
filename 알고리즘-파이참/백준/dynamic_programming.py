# # n = int(input())
# #
# # dp = [0 for _ in range(n+1)]
# # dp[1] = 0
# # # print(dp)
# # for i in range(2, n+1):
# #     dp[i] = dp[i-1] + 1
# #     if not i % 2 and dp[i] > dp[i//2] + 1:
# #
# #         dp[i] = dp[i//2] + 1
# #     if not i % 3 and dp[i] > dp[i//3] + 1:
# #
# #         dp[i] = dp[i//3] + 1
# # print(dp[n])
#
# #
# # n = int(input())
# # dp = [0 for _ in range(n+1)]
# # dp[0] = 1
# # dp[1] = 1
# #
# # for i in range(2, n+1):
# #     dp[i] = dp[i-1] + dp[i-2]
# #
# # print(dp[n]%10007)
# #
#
#
# # n = int(input())
# # dp = [[0 for _ in range(10)] for _ in range(n+1)]
# #
# # for i in range(1,10):
# #     dp[1][i] = 1 # 1자리 수일때는 전부 1
# #
# # # 0, 9가 아니면 dp[n][m] = dp[n-1][m-1] + dp[n-1][m+1]
# # #  0이면 dp[n] =
# #
# # for i in range(2, n+1):
# #     for j in range(10):
# #         if j-1 >= 0:
# #             dp[i][j] += dp[i-1][j-1]
# #         if j + 1 <= 9:
# #             dp[i][j] += dp[i-1][j+1]
# # ans = 0
# # for i in range(10):
# #     ans += dp[n][i]
# #
# # print(ans % 1000000000)
#
#
# n = int(input())
#
# dp = [[0 for _ in range(10)] for _ in range(n+1) ]
#
# for i in range(10):
#     dp[1][i] = 1
#
# for i in range(2, n+1):
#     for j in range(10):
#         dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
#
# ans = 0
# for i in range(10):
#     ans += dp[n][i]
#
# print(ans%10007)


from typing import List

Vector = List[float]

def ss(scalar:float, vector:Vector) -> Vector:
    return [scalar* num for num in vector]

new_vector = ss(2.0, [1.0,2.1])
print(new_vector)