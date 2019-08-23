import sys
sys.stdin = open('섬.txt', 'r')

def move(ls, stack, x, y, count): # 리스트와 x, y 좌표 카운트 값 설정 상하좌우로 이동하는 모든 경우를 설정해야 한다.그리고 범위 역시 지정해줘야 한다.
    dx = [1,0,-1,0,1,1,-1,-1]
    dy = [0,1,0,-1,1,-1,1,-1]
    ls[x][y] = 0 # 들어온 지점을 0으로 변경함
    while stack:
        for i in range(8): ### matrix 내에서 이동을 아직 구현하지 못했습니다.
            new_x = x + dx[i]
            new_y = y + dy[i] # 한 지점을 둘러싼 지역에 숫자가 있는지 확인
            if ls[new_x][new_y] != 0:
                stack.add((new_x,new_y)) # 향후 다시 스택으로 돌아가기 위해, 중복 방지를 위해 set 사용
        if ls[x+dx[0]][y] != 0:
            return down(ls, stack, x+dx[0], y, count)
        elif ls[x+dx[0]][y] == 0:
            if ls[x+dx[2]][y] != 0:
                return up(ls, stack, x+dx[2], y, count)
            else:
                return right(ls, stack, x, y+dy[1], count)

        # elif ls[x+dx[0]][y] != 0 and ls[x + dx[x+dx[3]]][y] != 0:
        #     return up(ls, stack, x + dx[0], y, count)
        # # elif ls[x + dx[0]][y] != 0:
        #     return left(ls, stack, x + dx[0], y, count)
        # elif ls[x + dx[0]][y] != 0:
        #     return right(ls, stack, x + dx[0], y, count)

        else: # 0인경우 stack에서 하나씩 꺼내서 이 작업을 반복 해야한다.
            if stack:
                qu = stack.pop(0) #튜플로
                return move(ls, stack, qu[0], qu[1], count)
            else:
                break
    if not stack: # 모든 작업이 끝난 경우
        return count+1


def up(ls, stack, x, y, count):
    ls[x][y] = 0
    return move(ls, stack, x, y, count)
def down(ls, stack, x, y, count):
    ls[x][y] = 0
    return move(ls, stack, x, y, count)
def left(ls, stack, x, y, count):
    ls[x][y] = 0
    return move(ls, stack, x, y, count)
def right(ls, stack, x, y, count):
    ls[x][y] = 0
    return move(ls, stack, x, y, count)



#
# def find(ls, stack, x, y): # 지점의 주변에 1이 있는지 없는지 판단
#     dx = [1,0,-1,0,1,1,-1,-1]
#     dy = [0,1,0,-1,1,-1,1,-1]
#     for i in range(8)
#         new_x = x + dx[i]
#         new_y = y + dy[i] # 한 지점을 둘러싼 지역에 숫자가 있는지 확인
#         if ls[new_x][new_y] != 0:
#             stack.append((new_x,new_y))
#     return stack



test_num = int(input())
for tc in range(test_num):
    num = int(input())
    matrix = [[0] * num for _ in range(num)]
    for ls in range(num):
        matrix[ls] = list(map(int, input().split()))
    count = 0
    stack = {} # empty set 설정

    for x in range(8):
        for y in range(8):
            if matrix[x][y] != 0:
                count = move(matrix, stack, x, y, count)

    print(count)
