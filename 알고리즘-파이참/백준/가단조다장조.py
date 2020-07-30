string = list(input().split('|'))

stack = []

for k in string:
    stack.append(list(k))

# A B C D E F G
first = [0] * 2
second = [0] * 2

for kk in stack:
    if kk[0] == 'A' or kk[0] == 'D' or kk[0] == 'E':
        first[0] += 1
    elif kk[0] == 'C' or kk[0] == 'F' or kk[0] == 'G':
        first[1] += 1

    if len(kk) >= 2:
        if kk[-1] == 'A' or kk[-1] == 'D' or kk[-1] == 'E':
            second[0] += 1

        elif kk[-1] == 'C' or kk[-1] == 'F' or kk[-1] == 'G':
            second[1] += 1
if first[0] > first[1]:
    print('A-minor')
elif first[0] < first[1]:
    print('C-major')
else:
    if second[0] > second[1]:
        print('A-minor')
    elif second[0] < second[1]:
        print('C-major')