import sys
sys.stdin = open('5247.txt', 'r')

from collections import deque

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    visited = [0] * 1000000
    queues = deque()
    queues.append([N, 0])
    while queues[-1][0] != M:
        if not visited[queues[0][0]]:
            if queues[0][0] > M:
                if 0 < queues[0][0] - 1 <= 1000000:
                    queues.append([queues[0][0] - 1, queues[0][1] + 1])
                    if queues[-1][0] == M:
                        break
                if 0 < queues[0][0] - 10 <= 1000000:
                    queues.append([queues[0][0] - 10, queues[0][1] + 1])
                    if queues[-1][0] == M:
                        break
                visited[queues[0][0]] = 1
            else:
                if 0<queues[0][0]-1<=1000000:
                    queues.append([queues[0][0]- 1, queues[0][1]+1])
                    if queues[-1][0] == M:
                        break
                if 0<queues[0][0]-10<=1000000:
                    queues.append([queues[0][0]- 10, queues[0][1]+1])
                    if queues[-1][0] == M:
                        break
                if 0<queues[0][0]+1<=1000000:
                    queues.append([queues[0][0] + 1, queues[0][1]+1])
                    if queues[-1][0] == M:
                        break
                if 0 < queues[0][0] *2 <= 1000000:
                    queues.append([queues[0][0] * 2, queues[0][1]+1])
                    if queues[-1][0] == M:
                        break
                visited[queues[0][0]] = 1
        queues.popleft()

    print('#{} {}'.format(t+1, queues[-1][1]))