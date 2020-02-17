from itertools import permutations

N = int(input())
list_number = list(map(int, input().split()))

max_cnt = 0

for k in permutations(list_number):
    circle = [0] * N
    summ = 0
    cnt = 0
    for i in range(N):
        summ += k[i]
        circle[i] = summ
    for i in range(N):
        if circle[i] + 50 in circle:
            cnt += 1
            if circle[i] > 51:
                break
    if cnt > max_cnt:
        max_cnt = cnt
    # print(circle)
print(max_cnt)