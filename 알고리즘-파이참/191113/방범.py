import sys
sys.stdin = open('방범.txt', 'r')

def iswall(x,y):
    return 0 <= x < N and 0 <= y < N

def make_range(R):
    global max_value, dxdys
    for i in range(N):
        for j in range(N):
            cost = R**2 + (R - 1) ** 2
            if R == 1:
                if city[i][j] == 1:
                    res = M - cost
                    if res > 0:
                        max_value = 1
                else:
                    pass

            else:
                cnt = 0
                cnt2 = 0
                visited = [ [0]*N for _ in range(N)]
                visited[i][j] = 1
                stack = [(i, j)]
                for k in stack:
                    if cnt2 == R-1:
                        break
                    for dxdy in dxdys:
                        dx, dy = k[0]+dxdy[0], k[1]+dxdy[1]
                        if iswall(dx, dy) and not visited[dx][dy]:
                            stack.append((dx,dy))
                    cnt2 += 1
                for k in stack:
                    if city[k[0]][k[1]] == 1:
                        cnt += 1
                        visited[k[0]][k[1]] = 1

                res = cnt*M - cost
                if res > 0:
                    if cnt > max_value:
                        max_value = cnt


tc = int(input())
for tn in range(1,tc+1):
    N, M = map(int, input().split()) # N = 도시 크기,  M 은 한 집이 낼 수 있는 최대 비용
    city = [list(map(int, input().split())) for _ in range(N)]

    # 범위
    dxdys = [(1,0), (-1,0), (0,1), (0,-1)]

    max_value = 0
    for n in range(1, (N+2)):
        make_range(n)
    print('#%d %d' %(tn, max_value))