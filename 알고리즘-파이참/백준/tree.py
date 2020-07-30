def iswall(x, y):
    return 0 <= x < n and 0 <= y < n

n, m, k = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(n)] # 땅
tree = [ [[] for _ in range(n)] for _ in range(n) ] # 나무
ground = [[5]*n for _ in range(n)]

for _ in range(m):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)
    # 나무 심었음

#k년이 지난 후 살아남은 나무
# 1. 봄에는 자신의 나이만큼 양분을 먹고 나이가 증가 여러개면 어린거 부터,
# 양분이 부족해 나이만큼 양분을 못 먹으면 즉시 죽는다

# 여름엔 죽은 나무가 양분으로 나이를 2로 나누고 소수점 버림
# 가을에는 번식한다 번식나무는 나이가 5의 배수이어야함 인접 8개에 1인 나무가 생김
#겨울엔 땅에 양분을 추가한다.
# 처음 arr에 들어온 값으로 양분이 추가된다.

dxdy = [(1,0), (0,1), (-1,0), (0,-1),
        (1,1), (-1,-1),(-1,1), (1,-1)]

for _ in range(k):
    # 봄 여름
    for i in range(n):
        for j in range(n):
            if len(tree[i][j]) <= 0: continue
            tree[i][j].sort()
            idx = 0
            while idx<len(tree[i][j]):
                if tree[i][j][idx]<=ground[i][j]:
                    ground[i][j]-=tree[i][j][idx]
                    tree[i][j][idx] += 1
                    idx+=1
                else:
                    die = tree[i][j][idx:]
                    for now in die:
                        ground[i][j] += (now/2)
                    tree[i][j] = tree[i][j][:idx]
                    break
    #가을
    for i in range(n):
        for j in range(n):
            c = 0
            if tree[i][j]:
                for now in tree[i][j]:
                    if now%5 == 0:
                        c+=1
            if c > 0:
                for dx, dy in dxdy:
                    new_i, new_j = i + dx, j + dy
                    if iswall(new_i, new_j):
                        for _ in range(c):
                            tree[new_i][new_j].append(1)
    # 겨울
    for i in range(n):
        for j in range(n):
            ground[i][j] += arr[i][j]

answer = 0
for i in range(n):
    for j in range(n):
        answer += len(tree[i][j])

print(answer )