# print(word == word[::-1])

import sys

sys.stdin = open('4861.txt','r')

#이중배열
def find_par(ls1, garow, sen_num):

    if sen_num == garow:
        for a in range(garow):
            sero = []
            garo = []
            for b in range(garow):
                garo.append(ls1[a][b])
                sero.append(ls1[b][a])


            print(garo[::-1], garo)
            if garo == garo[::-1]:
                return garo
            elif sero == sero[::-1]:
                return sero
    # else:
    #     for i in range(len(case)-sen_num):
    #






for _ in range(int(input())):
    N, M = map(int,input().split())
    club = []
    for i in range(N):
        case = list(input())
        club.append(case)
    find_par(club, N, M)