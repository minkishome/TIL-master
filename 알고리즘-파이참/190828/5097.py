import

t_n = int(input())

for tc in range(t_n):
    info = tuple(map(int,input().split()))
    ls = list(map(int,input().split()))

    a = info[1]%info[0]
    print('#%d %d' %(tc+1, ls[a]))