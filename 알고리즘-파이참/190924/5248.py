import sys
sys.stdin = open('5248.txt', 'r')


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


