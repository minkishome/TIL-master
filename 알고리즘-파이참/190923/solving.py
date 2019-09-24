def how_many(ls, a):
    if a == 2:
        return
    k = len(ls)

    for _ in range(k):
        b = ls.pop(0)
        for i in ls_friends:
            if i[0] == b and i[1] != 1:
                ls_cnt.add(i[1])
            if i[1] == b and i[0] != 1:
                ls_cnt.add(i[0])

    if ls_cnt:
        ls = list(ls_cnt)
        how_many(ls, a + 1)
    else:
        return


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    ls_friends = [list(map(int, input().split())) for _ in range(M)]
    ls_rel = [1]
    ls_cnt = set()
    how_many(ls_rel, 0)
    print('#%d %d' % (tc, len(ls_cnt)))
