N = int(input()) # 지원자 수
ls_t = [0 for i in range(0,151)]
for i in range(N):
    a, b = map(int, input().split())
    for k in range(a,b):
        ls_t[k] += 1
print(max(ls_t))