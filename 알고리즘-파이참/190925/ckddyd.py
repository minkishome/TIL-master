import sys
sys.stdin = open('ckddyd.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    group = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        group[a][b] = 1
        group[b][a] = 1
    # 갈 수 있는 지역 찾음
    check = [False] * (N+1)
    check[0] = 1
    stack = []
    cnt = 0

    for i in range(1, N+1):
        if not check[i]:
            stack.append(i)
            cnt += 1
            check[i] = True

        while stack:
            for k in range(N+1):
                if group[stack[0]][k] and not check[k]:
                    stack.append(k)
                    check[k] = True
            else:
                stack.pop(0)
    print('#%d %d' %(tc, cnt))
