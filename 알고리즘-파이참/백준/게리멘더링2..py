def sum_peo1(x,y, d1, d2):
    summ = 0
    for i in range(0, x + d1):
        for j in range(0, y+1):
            summ += arr[i][j]
    summ2 = 0
    t = -1
    for k in range(x, x+d1):
        t += 1
        for l in range(y-t, y+1):
            summ2 += arr[k][l]
    summ -= summ2
    return summ
def sum_peo2(x,y, d1, d2):
    summ = 0
    for i in range(0, x + d2+1):
        for j in range(y+1,N):
            summ += arr[i][j]
    summ2 = 0
    t = 0
    for k in range(x+1, x+d2+1):
        t += 1
        for l in range(y+1, y+1+t):
            summ2 += arr[k][l]
    summ -= summ2
    return summ
def sum_peo3(x,y, d1, d2):
    summ = 0
    for i in range(x+d1, N):
        for j in range(0, y-d1+d2):
            summ += arr[i][j]
    summ2 = 0
    t = -1
    for k in range(x+d1, x+d1+d2+1):
        t += 1
        for l in range(y-d1+t, y-d1+d2):
            summ2 += arr[k][l]
    summ -= summ2
    return summ
def sum_peo4(x,y, d1, d2):
    summ = 0
    for i in range(x + d2+1, N):
        for j in range(y-d1+d2, N):
            summ += arr[i][j]
    summ2 = 0
    t = -1
    for k in range(x+d2+1, x+d1+d2+1):
        t += 1
        for l in range(y-d1+d2, y+d2-t):
            summ2 += arr[k][l]
    summ -= summ2
    return summ

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
total = 0
for k in arr:
    total += sum(k)

min_value = 99999999
for x in range(N-2):
    for y in range(1,N-1):
        for d1 in range(1,y+1):
            for d2 in range(1, N-y):
                try:
                    ls_ppp = []
                    ls_ppp.append(sum_peo1(x,y,d1,d2))
                    ls_ppp.append(sum_peo2(x,y,d1,d2))
                    ls_ppp.append(sum_peo3(x,y,d1,d2))
                    ls_ppp.append(sum_peo4(x,y,d1,d2))
                    ls_ppp.append(total - sum(ls_ppp))
                    ls_ppp.sort()
                    if min_value > ls_ppp[-1] - ls_ppp[0]:
                        min_value = ls_ppp[-1] - ls_ppp[0]
                except:
                    break
print(min_value)