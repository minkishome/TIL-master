N = int(input())

ls_weight = [0] * N
ls_kee = [0] * N
ls_total = [0] * N
for i in range(N):
    a, b = map(int, input().split())
    ls_weight[i] = [a, i+1]
    ls_kee[i] = [b, i+1]
    # ls_total[i] = [a,b]
check = [0] * (N)
check2 = [0] * N
ls_kee.sort(reverse = True)
ls_weight.sort(reverse = True)
print(ls_kee, ls_weight)
a = 1
for i in range(N):
    print(check2)
    check[ls_kee[i][1]-1] += 1
    check[ls_weight[i][1]-1] += 1

    if 2 in check and 1 not in check:
        for j in range(N):
            if check[j] == 2:
                check2[j] = a
                check[j] = 0

        a += check2.count(a)
print(' '.join(map(str, check2)))
#     for j in range(N):
#         if ls_total[j][2] == 2:
#             for k in ls_total:
#
#
#             check[j] = a
#             ls_total[j][2] = 0
#             a += 1
#             # for k in ls_total:
#             #     if 1 not in k:
#             #
# print(check)

