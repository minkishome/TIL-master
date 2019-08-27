path = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
for j in path:

path2 = [0] * (len(path)//2)
for i in range(len(path)//2):
    path2[i] = (path[2*i], path[2*i+1])

visit = [1]
que = [1]
while que:
    a = que.pop(0)
    for i in path2:
        if a == i[0]:
            if not i[1] in visit:
                que.append(i[1])
                visit.append(i[1])
                print(visit, que)

print(visit)
