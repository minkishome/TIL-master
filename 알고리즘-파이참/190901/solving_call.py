import sys
sys.stdin = open('solving_call.txt', 'r')

for tc in range(1, 11):
    N, num = map(int, input().split())
    ls = list(map(int, input().split()))

    call = {ls[2*i]: [] for i in range(len(ls)//2)}
    for i in range(len(ls)//2):
        call[ls[2 * i]] += [ls[2 * i + 1]]
    ls_final = []
    que = []
    ls_check = []
    que.append(call[num])
    ls_check.append(num)
    ls_final.append(call[num])
    while que:
        ls_plus = []
        ls_que = que.pop(0)
        for i in ls_que:
            if i in call.keys():
                for j in call[i]:
                    if j not in ls_check:
                        ls_plus.append(j)
                        ls_check.append(j)
        if ls_plus != []:
            que.append(ls_plus)
            ls_final.append(ls_plus)

    print('#%d %d' %(tc, max(ls_final[-1])))