N = int(input())
ls = list(map(int, input().split()))
ls_seat = []
a = 0
for i in range(len(ls)):
    if ls[i] == 1:
        ls_seat.append(i)

max_val = 0
alpha = len(ls_seat)
for i in range(alpha-1):
    find = (ls_seat[i+1] +ls_seat[i])//2
    val1 =  ls_seat[i+1] - find
    val2 =  find - ls_seat[i]
    val = min(val1, val2)
    if val > max_val:
        max_val = val
if ls[-1] == 0:
    edge1 = (len(ls)-1) - ls_seat[-1]
    if max_val < edge1:
        max_val = edge1
if ls[0] == 0:
    edge2 = ls_seat[0]
    if max_val < edge2:
        max_val = edge2
print(max_val)