import sys
sys.stdin = open('solving.txt', 'r')

def check(i,j, N):
    global ls, ls1
    a = i
    b = j
    while i < N:
        if ls[i][j] == 0:
            break
        i += 1
    while j < N:
        if ls[a][j] == 0:
            break
        j += 1


    for x in range(a, i):
        for y in range(b, j):
            ls[x][y] = 0 # 수행한 길을 모두 0으로 만들어준다.
    return ls1.append((i-a,j-b)) # ls1에 찾은 범위를 넣어준다.

test_num = int(input())

for tc in range(1, test_num+1):
    N = int(input())
    ls = [list(map(int,input().split())) for _ in range(N)]
    ls1 = []

    for i in range(N):
        for j in range(N):
            if ls[i][j] != 0:
                check(i,j, N)
    a = len(ls1)
    ls2 = [0] * a
    ls3 = [0] * a
    for i in range(len(ls1)-1):
        min = i
        for j in range(i+1, len(ls1)):
            if ls1[min][0]*ls1[min][1] < ls1[j][0]*ls1[j][1]:
                min = j
            ls1[min], ls1[j] = ls1[j], ls1[min]
    # for i in range(len(ls1)-1):
    #     for j in range(i+1, len(ls1)):
    #         if ls1[i][0] * ls1[i][1] == ls1[j][0] * ls1[j][1]:
    #             c = ls1[i][0]
    #             d = ls1[j][0]
    #             if c < d:
    #                 pass
    #             elif d < c:
    #                 ls1[i], ls1[j] = ls1[j], ls1[i]
    string = ''
    # print(ls1)
    result = []
    for i in range(len(ls1)):
        result.append([ls1[i][0], ls1[i][1], int(ls1[i][0])*int(ls1[i][1])])
    # print(result)
    for i in range(len(ls1)-1):
        for j in range(i, len(ls1)):
            if result[i][2] > result[j][2]:
                result[i], result[j] = result[j], result[i]
            if result[i][2] == result[j][2]:
                if result[i][0] > result[j][0]:
                    result[i], result[j] = result[j], result[i]
    # print(result)
    # for i in ls1:
    #     string += ' '+str(i[0])+' '+str(i[1])
    # print('#%d %d%s' %(tc,a,string))
    print('#{} '.format(tc), end='')
    print('{} '.format(len(result)), end='')
    for i in range(len(result)):
        print('{} {} '.format(result[i][0], result[i][1]), end='')
    print()

