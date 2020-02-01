def find(lsls, z):
    ls2 = lsls[:]
    if z == M:
        z = 0
        for i in range(M - 1):
            if lsls[i] <= lsls[i + 1]:
                z += 1
        if z == M - 1:
            for i in lsls:
                print(i, end= ' ')
            print()
    else:
        for i in range(1, N+1):
            ls2.append(ls[i])
            find(ls2, z+1)
            ls2.pop(-1)



N, M = map(int,input().split())
ls = [0] * (N+1)
for i in range(1,N+1):
    ls[i] = i
visited = [False] * (N+2)
ls3 = []
find(ls3, 0)