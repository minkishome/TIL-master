n = int(input())

arr = [list(input()) for _ in range(n)]

namu = []
fin = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'B':
            namu.append((i,j))
        elif arr[i][j] == 'E':
            fin.append((i,j))
# 나무랑 fin에 넣고

dxdy = [(1, 0), (0, 1), (-1, 0), (-1, 0), 'turn']

visited = [[[0]*3 for _ in range(n)] for _ in range(n) ]

# 회전은 중간에서 뻗어나가는 거로?

# if k == 'turn':
#     namu[0], namu[2] = namu[1] + dxdy[0][0], namu[2] + dxdy[2][0]
#     namu[0], namu[2] = namu[1] + dxdy[1][1], namu[2] + dxdy[3][1]
#     이 둘중 하나로 이동해야한다.