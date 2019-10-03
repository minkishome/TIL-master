N = input()

b = len(N)
M = int(N)
if M <= 19:
    num = 1
else:
    num = M - 9*b

res = 0
for i in range(num, M):
    sum = i
    num2 = i
    while num2 != 0:
        c = num2 % 10
        num2 = num2 // 10
        sum += c
    if sum == M:
        res = i
        break
print(res)
