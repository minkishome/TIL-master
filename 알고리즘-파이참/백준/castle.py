from collections import deque
from itertools import combinations

def attack(ls, n_archer):
    global max_val, n, m ,d
    k = 0
    list_attack = []
    archer = deque([0, 0, 0])
    for i in range(3):
        archer[i] = [n, n_archer[i]]
    while k < n:
        for kk in archer:
            for j in range(len(ls)): # 범위로 바꾸고
                if ls[j] != [1000, 1000] and abs(kk[0]-ls[j][0])+abs(kk[1]-ls[j][1]) <= d:
                    list_attack.append(ls[j])
                    ls[j] = [1000, 1000]
                    break
        k += 1
        for q in range(len(ls)):
            if ls[q] != [1000, 1000]:
                ls[q][0] += 1
                if ls[q][0] == n:
                    ls[q] = [1000, 1000]

    # 공격당한 적의 수는 len(list_attack)
    # print(list_attack)
    # print(123123123)
    if max_val < len(list_attack):
        max_val = len(list_attack)
    # print(max_val)
    # print('------')
    return

def dfs():
    return

n, m, d = map(int, input().split())

enemy = deque(list(map(int, input().split())) for _ in range(n)) # 적
enemy_spot = []
archer = deque([0]*m)
max_val = 0
for i in range(n-1, -1, -1):
    for j in range(m):
        if enemy[i][j] == 1:
            enemy_spot.append([i, j])
print(enemy_spot)
ls = combinations(range(n), 3)
for k in ls:
    print(k)
    attack(enemy_spot, k)

print(max_val)