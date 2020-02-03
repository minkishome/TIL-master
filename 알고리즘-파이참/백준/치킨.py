import sys, itertools
sys.stdin = open('치킨.txt', 'r')

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


