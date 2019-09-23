import sys
sys.stdin = open('no_friends.txt', 'r')

def how_many(ls, a):
    if a == 2:
        return
    k = len(ls)

    for _ in range(k):
        b = ls.pop(0)
        for i in ls_friends:
            if i[0] == b:
                ls_cnt.add(i[1])

    if ls_cnt != {}:
        ls = list(ls_cnt)
    how_many(ls, a+1)



for tc in range(1,int(input())+1):
    N, M = map(int, input().split())
    ls_friends = [list(map(int,input().split())) for _ in range(M)]
    ls_rel = [1]
    ls_cnt = set()
    how_many(ls_rel,0)
    # print(ls_cnt)
    print('#%d %d' %(tc, len(ls_cnt)))