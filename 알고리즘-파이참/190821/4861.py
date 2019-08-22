# print(word == word[::-1])

import sys

sys.stdin = open('4861.txt','r')

#이중배열
def find_par(ls1, garow, sen_num):
    #가로에 대한 확인
    for i, k in range(garow):
        for j, u in range(garow-sen_num+1):
            ls2 = ls1[i][j:j+sen_num+1]
            ls3 = ls1[j:j+sen_num+1][i]
            if ls2 == ls2[::-1]:
                return ls2
            elif ls3 == ls3[::-1]:
                return ls3
    # for k in range(garow):
    #     for z in range(garow-sen_num+1):
    #         ls3 = []
    #         for num in range(sen_num):
    #             ls3 += ls1[z+num][k]
    #         if ls3 == ls3[::-1]:
    #             return ls3





    # if sen_num == garow:
    #     for a in range(garow):
    #         sero = []
    #         garo = []
    #         for b in range(garow):
    #             garo.append(ls1[a][b])
    #             sero.append(ls1[b][a])
    #
    #
    #         print(garo[::-1], garo)
    #         if garo == garo[::-1]:
    #             return garo
    #         elif sero == sero[::-1]:
    #             return sero
    # else:
    #     for i in range(len(case)-sen_num):
    #





tc = int(input())
for num in range(tc):
    N, M = map(int,input().split())
    ls_case = []
    for i in range(N):
        case = list(input())
        ls_case.append(case)
    ls_final = ''.join(find_par(ls_case, N, M))
    print('#%d %s' %(num+1, ls_final))
