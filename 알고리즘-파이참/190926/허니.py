import sys, copy
sys.stdin = open('허니.txt', 'r')

def make_ls(ls):
    global N, M
    for i in range(N):
        for j in range(N-M+1):
            ls_2 = []
            for k in range(M):
                ls_2.append(ls[i][j+k])
            ls_3.append(ls_2)

def make_line(ls, lsls):
    global C, max_part

    A = sum(lsls)
    if A <= C:
        if max_part < A:
            b = 0
            for i in lsls:
                b += i*i
                ls_5.add(b)
        for i in range(0, M):
            if not check[i]:
                check[i] = True
                lsls.append(ls[i])
                make_line(ls, lsls)
                lsls.pop(-1)
                check[i] = False




def make_sqr(ls):
    global ls_5
    for i in ls:
        if sum(i) <= C:
            a = 0
            for j in i:
                a += j*j
            ls_4.add(a) # 제곱의 가장 큰 갑
        else: # C 보다 크기에 최대한 근접한 조합으로 만들어준다.
            lsls = []
            # max_ls = []
            ls_5 = set()
            make_line(i, lsls)
            ls_5 = list(ls_5)
            b = max(ls_5)
            ls_4.add(b)
            # b = 0
            # for k in max_ls:
            #     b += k*k
            # ls_4.append(b)


for tc in range(1, int(input())+1):
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]
    ls_3 = []
    make_ls(honey)
    print(ls_3)
    ls_4 = set()
    check = [False] * (M+1)
    max_part = 0
    make_sqr(ls_3)
    ls_4 = list(ls_4)
    ls_4.sort()

    # print('#%d %d' %(tc,ls_4[-1] + ls_4[-2]))
