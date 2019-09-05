import sys, itertools
sys.stdin = open('치킨.txt', 'r')
#
#
# def find_store(ls_store, ls_house):
#     min_value = 1000
#     for i in ls_store:
#


# def getSubset(lst):
#     n = len(lst)
#     ls_part = []
#     for i in range(1<<n): # i: 0000, 0001, 0010, 0011, 0100, 0101, 0110, 0111
#         for j in range(n): # j: 0001, 0010, 0100
#             t_f = i & (1 << j)
#             if t_f: # t_f 가 0 이 아닌 경우에는 출력.
#
#                 print(lst[j], end=' ') # 0, 1, 2
#                 ls_part.append(lst[j])
#         print()

N, M = map(int, input().split())
mapa = [ list(map(int, input().split())) for _ in range(N)]

ls_store = []
ls_house = []

for i in range(N):
    for j in range(N):
        if mapa[i][j] == 2:
            ls_store.append([i+1, j+1])
        if mapa[i][j] == 1:
            ls_house.append([i+1, j+1])
# print(ls_house)
part_store = list(itertools.combinations(ls_store, 2))

print(part_store)
for i in part_store:
    print(i)
    print(i[0], i[1])
print(ls_house)


