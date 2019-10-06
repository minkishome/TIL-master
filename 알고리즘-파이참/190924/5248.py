import sys
sys.stdin = open('5248.txt', 'r')

<<<<<<< HEAD
def find(dict_a, keys):
    global N, cnt
    if check[keys] == 0:
        cnt += 1
        check[keys] = 1
        if dict_a[keys]:
            for k in dict_a[keys]:
                check[k] = 1
                find(dict_a, k)
    elif dict_a[keys]:
        for k in dict_a[keys]:
            check[k] = 1
            find(dict_a, k)




for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    ls = list(map(int, input().split()))
    ls_party = [sorted([ls[2*i], ls[2*i+1]]) for i in range(M) ]
    ls_part = [ [] for _ in range(M) ]
    ls_part[0] = ls_party[0]
    check = [0] * (N+1)
    dict_part = { i+1 : []  for i in range(N)}
    cnt = 0
    for i in ls_party:
        if i[0] in dict_part.keys():
            dict_part[i[0]] += [i[1]]
        elif i[1] in dict_part.keys():
            dict_part[i[1]] += [i[0]]
    for i in range(1,N+1):
        find(dict_part, i)
    print('#%d %d' %(tc, cnt))
=======

def find(x): # group index
    for g in range(len(group)):
        if x in group[g]:
            return g
    return None

T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    people = set(list(range(1, n+1)))
    cnt = len(people - set(data))
    group = []
    for i in range(len(data)//2):
        if find(data[i*2])!= None and find(data[i*2+1])!= None:
            if find(data[i*2])!= find(data[i*2+1]):
                group[find(data[i*2])].update(group.pop(find(data[i*2+1])))
        elif find(data[i*2]) != None:
            group[find(data[i * 2])].add(data[i*2+1]) #group[1].add
        elif find(data[i*2+1])!= None:
            group[find(data[i * 2+1])].add(data[i*2])
        else:
            group.append(set([data[i*2], data[i*2+1]]))
    print("#{} {}".format(tc+1, cnt+len(group)))


>>>>>>> 9f447de86b6a39358272937d12b01f8478a0f10b
