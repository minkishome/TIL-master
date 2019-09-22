N,M = map(int, input().split())
ls = [0]*N
for i in range(N):
    ls[i] = int(input())

ls_check = [[0] for _ in range(M)]
cnt = 0
for i in range(M):
    ls_check[i] = [ls[0]]
    ls.pop(0)
b = 0
while 1:
    cnt += 1
    for j in ls_check:
        if j[-1] == cnt:
            if ls != []:
                a = ls.pop(0)
                j.append(a)
            b = 1
    if b == 1:
        cnt = 0
        b = 0
    if ls == []:
        break
max_sum = 0
for k in ls_check:
    if sum(k) > max_sum:
        max_sum = sum(k)
print(max_sum)