def iswall(x, y):
    return 0 <= x < N and 0 <= y < M


# def clean(direc, x, y, cnt, check):  # 방향, 카운트
#     # 먼저 방향을 잡아야한다.
#     if check == 4:
#         over_two(direc, x, y, cnt, check)
#     if direc != 0:
#         direc -= 1
#     else:  # 0일떄
#         direc = 3
#         # 방향 전환
#     new_x = x + dxdy[direc][0]
#     new_y = y + dxdy[direc][1]
#     if iswall(new_x, new_y) and not visited[new_x][new_y] and not arr[new_x][new_y]:  # 방향 안, 방문 안했을때, 0일때
#         visited[new_x][new_y] = 1  # 방문
#         clean(direc, new_x, new_y, cnt + 1, check)
#     else:
#         clean(direc, x, y, cnt, check + 1)
#
#
# def over_two(direc, x, y, cnt, check):
#     if direc <= 1:
#         direc += 2
#     else:
#         direc -= 2
#     new_x, new_y = x + dxdy[direc][0], y + dxdy[direc][1]
#     if iswall(new_x, new_y) and not arr[new_x][new_y]:
#         clean(direc, new_x, new_y, cnt, 0)
#     elif not iswall(new_x, new_y) and arr[new_x][new_y]:
#         return cnt


N, M = map(int, input().split())
r, c, direction = map(int, input().split())  # (r,c) d는 방향 (0북, 1동 2남 3서)

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]  # 간 곳은 다시 가지 않는다
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            visited[i][j] = 1
dxdy = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # 왼쪽부터 시작해
visited[r][c] = 1
# 1 현재 위치 청소
# 2 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
# 3 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
# 4 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
# 5 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.

# counts = clean(direc, r, c, 0, 0)
# print(counts)
cnt = 0
x, y = r, c
check = 0
while 1:
    # print('pppppppppppppppppppppppppppppppp')
    if direction != 0:
        direction -= 1
        check += 1
    else:
        direction = 3
        check += 1
    new_x, new_y = x + dxdy[direction][0], y + dxdy[direction][1]
    if iswall(new_x, new_y) and not visited[new_x][new_y] and not arr[new_x][new_y]:
        visited[new_x][new_y] = 1
        x, y = new_x, new_y
        cnt += 1
        check = 0
        continue

    if check == 4: # 모두 청소가 되어있음
        if direction <= 1:
            direction += 2
        else:
            direction -= 2 # 후진
        new_x, new_y = x + dxdy[direction][0], y + dxdy[direction][1]
        if iswall(new_x, new_y) and not arr[new_x][new_y]:
            x, y = new_x, new_y
            check = 0
        elif not iswall(new_x, new_y) or arr[new_x][new_y]:
            break

print(cnt)



