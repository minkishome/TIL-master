import copy
def queen(ls, x, y, z): # y는 1씩 추가만 x만 바꿔가면서 변경

    global cnt
    ls2 = copy.deepcopy(ls)
    a = x
    b = y
    if z == n:
        cnt += 1
        return
    else:
        if ls2[x][y] == 0:
            ls2[x][y] = 2

            dx = [1, 1, 1, 0, 0, -1, -1, -1]  # 모든 방향 설정해줘야함
            dy = [1, -1, 0, 1, -1, -1, 1, 0]
            for i in range(8):
                k = 1
                while 1:
                    new_x = x + dx[i]*k
                    new_y = y + dy[i]*k
                    if 0 <= new_x < n and 0 <= new_y < n:
                        ls2[new_x][new_y] = 1
                        k += 1
                    else:
                        break
            for i in range(n):
                queen(ls2, z+1, i, z+1)



n = int(input())
matrix = [[0]*n for _ in range(n)]
cnt = 0
cnt2 = 0
check = [False] * (n+1)
for i in range(n):
    queen(matrix,0,i,0)
print(cnt)
print(matrix)
# ls = [[1,2,3],[4,5,6],[7,8,9]]
# print(ls[2][1])