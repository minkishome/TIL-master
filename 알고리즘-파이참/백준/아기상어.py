# 크면 못지나가고, 같으면 pass 못먹고, 작으면 먹는다
# 자신과 크기와 같은 수의 고기를 먹으면 크기 1 성장
from collections import deque
def iswall(x, y):
    return 0 <= x < n and 0 <= y < n

def dfs(shark, fish,  distance): # shark, fish의 좌표만 들어가야함
    global visited, baby, min_distance
    if distance < min_distance:
        for i in range(4):
            x, y = shark[0] + dxdy[i][0], shark[1] + dxdy[i][1]
            if iswall(x, y) and not visited[x][y] and arr[x][y] <= baby[0]: # 통과가능할때
                if fish[0] == x and fish[1] == y: # 도착했을 때
                    min_distance = distance
                else:
                    dfs([x, y], fish, distance + 1)

def dfss(shark, fish):
    global visited, baby, min_distance
    que = deque([(shark[0], shark[1])])
    while que:
        q = que.popleft()
        for i in range(4):
            x, y = q[0] + dxdy[i][0], q[1] + dxdy[i][1]
            if iswall(x, y) and not visited[x][y] and arr[x][y] <= baby[0]:  # 통과가능할때
                visited[x][y] = visited[q[0]][q[1]] + 1
                que.append((x, y))
                if fish[0] == x and fish[1] == y: # 도착했을 때
                    min_distance = visited[x][y]
                    return




n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dxdy = [(0,1), (1,0), (0,-1), (-1,0)]
baby = [2, 0, 0, 0]
fishes = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            pass
        else:
            if arr[i][j] == 9:
                baby = [2, i, j, 0]
            else:
                fishes.append([arr[i][j], i, j])

# 물고기와 관련된 내용을 넣음
flag = True
time = 0
while flag:
    visited = [[0] * n for _ in range(n)]
    min_distance = 100 # 함수에서 사용할 것
    min_value = 999 # 단순 거리 계산
    index = 9999
    for i in range(len(fishes)):
        if fishes[i][0] < baby[0] and fishes[i][0] != 0:
            dis = abs(baby[1]-fishes[i][1]) + abs(baby[2]-fishes[i][2]) # 조건이 여기가 아닌 dfss에 들어가야함
            if dis < min_value:
                min_value = dis
                index = i # 아기상어보다 작은 물고기가 어디있는지 확인\
    if index != 9999: # 작은 게 있을 때 가장 가까운 거리에 있는 물고기의 fishes 위치
        dfss([baby[1], baby[2]], [fishes[index][1], fishes[index][2]])
        if visited[fishes[index][1]][fishes[index][2]]:
            baby[1], baby[2] = fishes[index][1], fishes[index][2]
            baby[3] += 1
            if baby[3] == baby[0]:
                baby[0], baby[3] = baby[0] + 1, 0
            fishes[index][0] = 0
            time += min_distance


    else: # index가 똑같다는 것은 더 이상 변화가 없음 => 아기상어보다 작은 게 없다
        break


print(time)