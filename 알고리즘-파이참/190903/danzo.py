import sys
sys.stdin = open('danzo.txt', 'r')

def find(a,b):
    global max
    x = a * b
    if x > 10:
        for i in range(len(str(x)) - 1):
            if str(x)[i] > str(x)[i+1]:
                return
        if x > max:
            max = x
            return max
    else:
        return


for tc in range(int(input())):
    N = int(input())
    ls_check = []
    ls_find = []
    ls = list(map(int, input().split()))
    max = 1
    for i in range(len(ls)-1):
        for j in range(i+1, len(ls)):
            find(ls[i], ls[j])
            # a = ls[i]*ls[j]
            # b = str(a)
            # count_a = 0
            # if a > 10:
            #     for i in range(len(b)-1):
            #         if b[i] >= b[i+1]:
            #
            #
            #     if a > max:
            #         max = a
    print('#%d %d' % (tc + 1, max))


    #
    #         ls_check += [str(ls[i]*ls[j])]
    # for i in ls_check:
    #     if len(i) != 1:
    #         a = sorted(list(i))
    #         if a == list(i):
    #             ls_find.append(i)
    # # 리스트 안에 있는 str을 인트로 변경
    # for i in range((len(ls_find))):
    #     ls_find[i] = int(ls_find[i])
    # print('#%d %d' %(tc+1, max(ls_find)))

                # 각자 비교를 해주거나 아예 int로 전환했다가 솔트 했다가 다시 str로 바꾼게 같은 경우에만 ls_find로 넘긴다.

