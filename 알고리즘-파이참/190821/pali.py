import sys
sys.stdin = open('pali.txt', 'r')


# def palindrome(M):
#     max_length = 0
#     Flag = True
#     while Flag:
#         max_length += 1
#         count = 0
#         for i in range(100):
#             for j in range(101-max_length):
#                 garo = []
#                 sero = []
#                 for k in range(max_length):
#                     garo.append(M[i][k+j])
#                     sero.append(M[k+j][i])
#                 if garo == garo[::-1]:
#                     count += 1
#                     break
#                 if sero == sero[::-1]:
#                     count += 1
#                     break
#         if count == 0:
#             max_length += 1
#             for i in range(100):
#                 for j in range(101 - max_length):
#                     garo = []
#                     sero = []
#                     for k in range(max_length):
#                         garo.append(M[i][k + j])
#                         sero.append(M[k + j][i])
#                     if garo == garo[::-1]:
#                         count += 1
#                         break
#                     if sero == sero[::-1]:
#                         count += 1
#                         break
#             if count == 0:
#                 Flag = False
#                 return max_length -2
#
# # def palindrome(M):
# #     max_length = 101
# #     Flag = True
# #     while Flag:
# #         max_length -= 1
# #         for i in range(100):
# #             for j in range(101 - max_length):
# #                 garo = []
# #                 sero = []
# #                 for k in range(max_length):
# #                     garo.append(M[i][k + j])
# #                     sero.append(M[k + j][i])
# #                 if garo == garo[::-1]:
# #                     Flag = False
# #                     break
# #                 if sero == sero[::-1]:
# #                     Flag = False
# #                     break
# #     return max_length
# # for i in range(10):
# #     tc = int(input())
# #     M = [list(input()) for _ in range(100)]
#
#     res = palindrome(M)
#     print('#{} {}'.format(tc, res))








for _ in range(10):
    test_num = int(input())
    matrix = [list(input())for _ in range(100)]

    count = 0
    n = 101
    while count == 0:
        n -= 1
        for i in range(len(matrix)):
            ls4 = []
            for j in range(len(matrix) - n + 1):
                ls2 = matrix[i][j:j + n]
                for num in range(n):
                    ls4 += matrix[j + num][i]
                if ls4 == ls4[::-1] or ls2 == ls2[::-1]:
                    count += 1



        # # 세로에 대한 확인
        # for k in range(len(matrix)):
        #     for z in range(len(matrix) - n + 1):
        #         ls3 = []
        #         for num in range(n):
        #             ls3 += matrix[z + num][k]
        #         if ls3 == ls3[::-1]:
        #             count += 1

    print('#%d %d' %(test_num, n))


