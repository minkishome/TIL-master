# print(word == word[::-1])

import sys

sys.stdin = open('4861.txt','r')

#이중배열
def find_par(ls1, garo, sen_num):
    check2 = []
    check = []
    if sen_num == garo:
        for a in range(garo):
            for b in range(garo):
                check.append(ls1[a][b])
                check2.append(ls1[b][a])
                if check == check[::-1]:
                    return check
                if check2 == check2[::-1]:
                    return check2
    # else:
    #     for i in range(len(case)-sen_num):
    #






for _ in range(int(input())):
    N, M = map(int,input().split())
    club = []
    for i in range(N):
        case = list(input().split())
        club.append(case)
    print(find_par(club, N, M))