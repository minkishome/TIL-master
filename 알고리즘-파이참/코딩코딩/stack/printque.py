import collections
tc = int(input())

for q in range(tc):
    N, M = map(int,input().split())
    ls = list(map(int, input().split()))
    ls2 = []
    check = [0] * N
    for i in range(N):
        ls2.append([ls[i], i])
    cnt = 0
    # print(ls, ls2)
    a = max(ls)
    while cnt != N:
        for i in range(N):
            if ls[i] >= a:
                # print(a, cnt)
                check[cnt] = ls2[i]
                ls[i] = 0
                a = max(ls)
                cnt += 1
                if cnt == N:
                    break
    for j in range(N):
        if M == check[j][1]:
            print(j+1)
            break

