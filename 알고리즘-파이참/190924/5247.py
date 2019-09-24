import sys
sys.stdin = open('5247.txt', 'r')

# +1 -1 *2 -10

def do_someting(ls_do, b):
    global alpha
    if ls_check[M] != 0:
        return

    else:
        # ls_k = ls_do[len(ls_do)-d:]

        ls_k = []
        for a in ls_do:
            ls2 = [a+1, a-1, a-10, 2*a]
            for z in ls2:
                if 0 < z < 4*alpha:
                    if ls_check[z] == 0:
                        ls_check[z] = b
                        ls_k.append(z)
        do_someting(ls_k, b+1)



for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    alpha = max(N,M)
    ls_check = [0] * (4*alpha)
    visited = [0] * (4*alpha) # 처리해줘야함
    ls_do = [N]
    do_someting(ls_do,0)
    print('#%d %d' %(tc, ls_check[M]+1))





    # else:
    #     if min_val > c:
    #         if a*2 < b:
    #             return do_someting(2*a, b, c+1)
    #         else:
    #             if b - a < 10:
    #                 return do_someting(a+1, b, c+1)
    #             elif a - b < 10:
    #                 return do_someting(a-1, b, c+1)
    #

    # elif a*2 > b:
    #     if b - a > a*2 - b:
    #         do_someting(2*a -10, b, c+2)

