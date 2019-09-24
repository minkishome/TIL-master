import sys
sys.stdin = open('5248.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    ls = list(map(int, input().split()))
    ls_party = [sorted([ls[2*i], ls[2*i+1]]) for i in range(M) ]
    ls_part = [ [] for _ in range(M) ]
    ls_part[0] = ls_party[0]
    check = [0] * (N+1)
    dict_part = { i+1 : []  for i in range(N)}

    for i in ls_party:
        if i[0] in dict_part.keys():
            dict_part[i[0]] += [i[1]]
        elif i[1] in dict_part.keys():
            dict_part[i[1]] += [i[0]]
    print(dict_part, ls_party, check)
    cnt = 0
    for j in range(1,N+1):
        if check[j] == 0:
            cnt += 1
            check[j] = 1
            key = j
            while dict_part[key]:
                for k in dict_part[key]:
                    check[k] = 1

    print(cnt)