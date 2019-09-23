tin = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]
ls2 = []
for i in range(len(tin)//2):
    ls2.append([tin[2*i], tin[2*i+1]])

que = [1]
stack = [1]
while que:
    a = que.pop(0)
    for i in ls2:
        if a in i:
            if not i[1] in stack:
                que.append(i[1])
                stack.append(i[1])

print(stack)
