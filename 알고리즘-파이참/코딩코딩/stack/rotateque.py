import collections

def pop_same(a):
    global ls, cnt
    if a == M:
        return
    else:
        if ls_num[a] == ls[0]:
            number = ls.popleft()
            ls_check[a] = number
            pop_same(a+1)
        else:
            giri = len(ls)
            for j in range(N):
                if ls_num[a] == ls[j]:
                    if j > giri // 2:
                        return pop_right(a)
                    else:
                        return pop_left(a)


def pop_left(a):
    global ls, cnt
    while 1:
        if ls_num[a] == ls[0]:
            return pop_same(a)
        else:
            k = ls.popleft()
            ls.append(k)
            cnt += 1

def pop_right(a):
    global ls, cnt
    while 1:
        if ls_num[a] == ls[0]:
            return pop_same(a)
        else:
            k = ls.pop()
            ls.appendleft(k)
            cnt += 1


N, M = map(int, input().split())
ls_num = list(map(int, input().split()))

ls = collections.deque([0]*N)
for i in range(N):
    ls[i] = i+1

num = 0
cnt = 0
ls_check = [0] * M
pop_same(0)
print(cnt)

