import sys

sys.stdin = open('palindrome.txt', 'r')

def find_pali(ls,n):
    #가로에 대한 확인
    count = 0
    for i in range(len(ls)):
        for j in range(len(ls)-n+1):
            ls2 = ls[i][j:j+n]
            if ls2 == ls2[::-1]:
                count += 1
    #세로에 대한 확인
    for k in range(len(ls)):
        for z in range(len(ls)-n+1):
            ls3 = []
            for num in range(n):
                ls3 += ls[z+num][k]
            if ls3 == ls3[::-1]:
                count += 1
    return count
# def find_par(ls1, garow, sen_num):
#     #가로에 대한 확인
#     for i in range(garow):
#         for j in range(garow-sen_num+1):
#             ls2 = ls1[i][j:j+sen_num+1]
#             if ls2 == ls2[::-1]:
#                 return ls2
#     for k in range(garow):
#         for z in range(garow-sen_num+1):
#             ls3 = []
#             for num in range(sen_num):
#                 ls3 += ls1[z+num][k]
#             if ls3 == ls3[::-1]:
#                 return ls3




for _ in range(10):
    str_len = int(input())
    matrix = []
    for _ in range(8):
        ls_str = list(input())
        matrix.append(ls_str)
    print(find_pali(matrix, str_len))
