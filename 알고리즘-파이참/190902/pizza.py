import sys
sys.stdin = open('pizza.txt', 'r')

for tc in range(int(input())):
    N, M = map(int, input().split()) #N = 화덕의 크기 M = 피자의 갯수
    pizza = list(map(int, input().split()))
    for i in range(M):
        pizza[i] = [i+1, pizza[i]] # pizza[i][0]은 피자 순서 pizza[i][1]은 치즈 양
    num = N
    count = 0
    fire = [0] * N
    for i in range(N):
        if i > M:
            fire[i] = [999]
        fire[i] = pizza[i]
    print(pizza)

    while count != M-1:
        for i in range(len(fire)):
            if fire[i][1] != 0:
                fire[i][1] = int(fire[i][1]//2) # 모든 것의 피자를 반으로 줄인다.

                if fire[i][1] == 0:
                    count += 1
                    if num < M:
                        fire[i] = pizza[num]
                        num += 1


            if count == M - 1:
                break
    for i in range(len(fire)):
        if fire[i][1] != 0:
            a = fire[i][0]
    print('#%d %d' %(tc+1, a))
