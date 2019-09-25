import sys
sys.stdin = open('ckddyd.txt', 'r')


T = int(input())
for t in range(T):
    N, M = map(int, input().split())

    G = [[0] * (N + 1) for _ in range(N + 1)]

    for s in range(M):
        S, K = map(int, input().split())
        G[S][K] = 1
        G[K][S] = 1 #이차원 배열에 각각이 아는 사이면 넣어준다

    visited = [0] * (N + 1)

    stacks = []
    count = 0
    visited[0] = 1
    for i in range(1, len(visited)):
        if not visited[i]:
            stacks.append(i)
            count = count + 1
            visited[i] = 1

        while stacks:
            for idx in range(len(G[stacks[0]])): #1

                if G[stacks[0]][idx] and not visited[idx]:
                    stacks.append(idx)
                    visited[idx] = 1
            else:
                stacks.pop(0)

    print('#{} {}'.format(t + 1, count))




