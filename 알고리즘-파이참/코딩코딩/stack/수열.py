N = int(input())

ls_a = []
ls_check = []
ls_b = [0] * N
for i in range(N):
    ls_b[i] = int(input())
num = 0

for i in range(N):
    ls_a.append(i + 1)
    ls_check.append(1)

    if ls_b[num] == ls_a[-1]:
        while ls_b[num] == ls_a[-1]:
            ls_a.pop(-1)

            ls_check.append(2)
            num += 1
            if ls_a == []:
                break

if ls_a == []:
    for k in ls_check:
        if k == 1:
            print('+')
        else:
            print('-')
else:
    print('NO')


