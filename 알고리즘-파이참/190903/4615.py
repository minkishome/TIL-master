import sys

sys.stdin = open('4615.txt', 'r')


for tc in range(int(input())):
    N, M = map(int, input().split()) # N은 판의 크기, M은 놓는 횟수
    ls = [ [0]*N for _ in range(N)]
    dx = [0, -1, -1, -1, 0, 1, 1, 1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]

    a = int(N/2)
    ls[a-1][a-1] = 2
    ls[a-1][a] = 1
    ls[a][a-1] = 1
    ls[a][a] = 2
    # print(ls)
    for i in range(M):
        x1, y1, z = map(int, input().split()) # x는 x좌표, y는 y좌표 z는 흑 or 백
        x = x1 - 1
        y = y1 - 1
        ls[x][y] = z
        # for qq in range(N):
        #     print(ls[qq])
        # print('=======')
        for k in range(8):
            new_x = x + dx[k]
            new_y = y + dy[k]
            if 0 <= new_x < N and 0 <= new_y < N:
                if ls[new_x][new_y] != 0 and ls[new_x][new_y] != z:

                    ls1 = [[new_x, new_y]]
                    while 1:
                        new_x = new_x + dx[k]
                        new_y = new_y + dy[k]
                        if 0 <= new_x < N and 0 <= new_y < N:
                            if ls[new_x][new_y] != 0 and ls[new_x][new_y] != z:
                                ls1.append([new_x, new_y])
                            elif ls[new_x][new_y] == 0:
                                break # 0이 나올 경우 바꿀것이 없으므로 아무것도 변화시키지 않는다.
                            elif ls[new_x][new_y] == z:
                                for j in ls1:
                                    ls[j[0]][j[1]] = z
                                break
                        else:
                            break


    count_1 = 0
    count_2 = 0
    for j in range(N):
        count_1 += ls[j].count(1)
        count_2 += ls[j].count(2)
    print('#%d %d %d' %(tc+1, count_1, count_2))

    # while 1:
    #     x2 = new_x + dx[k]
    #     y2 = new_y + dy[k]
    #     if 0 <= x2 < N and 0 <= y2 < N:
    #         if ls[x2][y2] != 0 and ls[x2][y2] != z: # 0도 z도 아닌 경우 즉 다른 경우에는 z로 바꿔야함\]
    #
    #
    #
    #
    #             ls[x2][y2] = z
    #         else:
    #             break
    #     else:
    #         break

    #     if ls[new_x][new_y] != 0:
    #         if ls[new_x][new_y] != z: # 나랑 다를 경우
    #             ls[new_x][new_y] = z # 같은 값으로 변경한다.
    #
    #         # elif ls[new_x][new_y] == z: #만약에 같은 경우 while을 종료한다.
    #         #     break
    #     else:
    #         break
    # else:
    #     break
    # if ls[new_x][new_y] == 1:
    #     ls[new_x][new_y] = 2
    #     print(ls)
    # else:
    #     ls[new_x][new_y] = 1 # 색깔을 각각 바꿔준다.
    #     print(ls)
