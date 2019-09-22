N, M = map(str, input().split())
ls = []
for _ in range(int(N)):
    a, b = map(str, input().split())
    ls.append([int(a), list(map(int, b))])

print(ls)