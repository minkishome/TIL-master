import math

n = int(input())
room = list(map(int, input().split()))
b, c = map(int, input().split())
answer = 0
for i in range(n):
    answer += 1
    room[i] -= b
    if room[i] > 0:
        answer += math.ceil(room[i]/c)
print(answer)