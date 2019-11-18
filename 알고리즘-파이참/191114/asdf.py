import collections
import itertools
import queue
# ls = deque((1,2,3))
# print(ls)
# a = ls.popleft()
# print(a, ls)
#
# lsls = [1,2,3,4]
# cnt = 0
# for k in lsls:
#     cnt += 1
#     if cnt < 10:
#         lsls.append(5)
#         print(k)
#         print(lsls)

# lslsls = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
#
# ls2 = list(itertools.combinations(lslsls, 3))
# ls3 = list(itertools.permutations(lslsls, 3))
# ls4 = list(itertools.combinations_with_replacement(lslsls, 3))
# print(len(ls2))
# print(len(ls3))
# print(len(ls4))
# print(ls4)


lslsls = [1,2,3,4,5]
ls2 = list(itertools.combinations(lslsls,2))
print(ls2)

print('////////////////////////////')
# for k in ls4:
#     print(k)
# for k in ls2:
#     print(k)
# ls3 = itertools.permutations(lslsls,3)
T = [1,2,3,4,4,4,5,5,2,1,2,3]

idx = [1, 2, 3, 4]

# power_set = [[]]
# for i in idx:
#     tmp = [[i] + p for p in power_set]
#     power_set += tmp
#
#
# for i in range(2**(len(idx))):
#     print(power_set[i], power_set[-1-i])

power_set = [[]]
# for i in idx:
#     tmp = [[i] + p for p in power_set]
#     power_set += tmp
# for i in range(2**len(idx)):
    # print('%s \n%s' %(power_set[i], power_set[-1-i]) )

power_set2 = [[]]
for i in idx:
    tmp2 = [[i] + z for z in power_set2]
    power_set2 += tmp2
for i in range(2**len(idx)):
    print(power_set2[i], power_set2[-1-i])
ls123 = list(itertools.combinations(idx, 2))
ls1231234 = list(itertools.permutations(idx, 2))
print(ls123)
print(ls1231234)
print(ls123)


def observing(y, x, types, m):
    global longest
    if 0 <= m < 4:
        if not (0 <= y + dy[m] < size and 0 <= x + dx[m] < size):
            return

        if (y + dy[m], x + dx[m]) == (i, j):
            if len(types) > longest:
                longest = len(types)
                return
        if G[y + dy[m]][x + dx[m]] in types:
            return

        else:
            types.append(G[y + dy[m]][x + dx[m]]) # types == visit
            observing(y + dy[m], x + dx[m], types, m)
            observing(y + dy[m], x + dx[m], types, m + 1)
            types.pop()


dx = [-1, 1, 1, -1]
dy = [1, 1, -1, -1]

T = int(input())
for t in range(T):
    size = int(input())
    G = [list(map(int, input().split())) for _ in range(size)]
    longest = -1
    for i in range(size - 2): # 마지막 줄을 제외
        for j in range(1, size - 1):
            observing(i, j, [G[i][j]], 0)
    print('#{} {}'.format(t + 1, longest))

#////////////////////////////

def spread(x, y, cell, t):
    global vessel
    global check
    if not cell:
        return

    if cell[1] == 1 and t == cell[2] + cell[0] + 1:
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        for idx in range(4):
            new_x, new_y = x + dx[idx], y + dy[idx]
            if not vessel[new_y][new_x] or (vessel[new_y][new_x][2] == t and vessel[new_y][new_x][0] < cell[0]):
                vessel[new_y][new_x] = [cell[0], 0, t]
                check.append((new_x, new_y))

    if cell[1] != 2 and t == cell[2] + (cell[1] + 1) * cell[0]:
        cell[1] += 1


T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    grids = [list(map(int, input().split())) for _ in range(N)]
    vessel = [[0] * (M + 2 * K) for _ in range(N + 2 * K)]
    check = []

    for y in range(N):
        for x in range(M):
            if grids[y][x]:
                vessel[y + K][x + K] = [grids[y][x], 0, 0]
                check.append((x + K, y + K))

    for now in range(K + 1):
        for x, y in check:
            spread(x, y, vessel[y][x], now)

    result = 0
    for y in range(N + 2 * K):
        for x in range(M + 2 * K):
            if vessel[y][x] and vessel[y][x][1] != 2:
                result += 1

    print('#{} {}'.format(tc, result))









    def observing(y, x, types, m):
        global longest
        if 0 <= m < 4:
            if not (0 <= y + dy[m] < size and 0 <= x + dx[m] < size):
                return

            if (y + dy[m], x + dx[m]) == (i, j):
                if len(types) > longest:
                    longest = len(types)
                    return
            if G[y + dy[m]][x + dx[m]] in types:
                return

            else:
                types.append(G[y + dy[m]][x + dx[m]])
                observing(y + dy[m], x + dx[m], types, m)
                observing(y + dy[m], x + dx[m], types, m + 1)
                types.pop()


    dx = [-1, 1, 1, -1]
    dy = [1, 1, -1, -1]

    T = int(input())
    for t in range(T):
        size = int(input())
        G = [list(map(int, input().split())) for _ in range(size)]
        longest = -1
        for i in range(size - 2):
            for j in range(1, size - 1):
                observing(i, j, [G[i][j]], 0)
        print('#{} {}'.format(t + 1, longest))

idx = [1,2,3,4]
power_set3  = [[]]
for i in idx:
    tmp = [[i] + p for p in power_set3]
    power_set3 += tmp

for i in range(1,(2**len(idx))-1):
    print(power_set3[i], power_set3[-1-i])