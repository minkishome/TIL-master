from collections import deque

def iswall(x,y):
    return 0 <= x < N and 0 <= y < N


N = int(input())  # 배열 크기
K = int(input())  # 사과 갯수

arr = [[0]*N for _ in range(N)]
for _ in range(K):
    x, y = map(int,input().split())
    arr[x-1][y-1] = 1 # 사과
move = []
L = int(input())
for _ in range(L):
    x, y = input().split()
    move.append((int(x),y))
ls_move = [0] * (move[-1][0] + 2)
the_longest_move = move[-1][0]
for k in move:
    ls_move[k[0]] = k[1] # L or R로 나눠서 생각
direction = [(-1,0), (0,1), (1,0), (0,-1)]
snake= deque([(0,0)])
# print(snake)
# head = snake[0]
time = 0
Flag = True
direc = 1
while Flag:
    #시작은 direction[1]
    # time += 1
    new_head = (snake[-1][0]+direction[direc][0], snake[-1][1] + direction[direc][1])
    # print(time, snake )
    # print(new_head[0],new_head[1])
    if iswall(new_head[0], new_head[1]):
        if (new_head[0],new_head[1]) in snake:
            Flag = False
            break
        else:
            snake.append(new_head) 
            if arr[new_head[0]][new_head[1]] == 0:
                snake.popleft()
            else:
                arr[new_head[0]][new_head[1]] = 0
                # pass # 사과면 빼지 말고
            time += 1
            if time <= the_longest_move:
                if ls_move[time] != 0:
                    # print(direc, ls_move[time])
                    if ls_move[time] == 'L':
                        if direc != 0:
                            direc -= 1
                        else:
                            direc = 3
                    else: #R
                        if direc != 3:
                            direc += 1
                        else:
                            direc = 0    # 방향도 바꿔줌
                # print(direc)
        
    else:       
        Flag = False
        break
print(time+1)
