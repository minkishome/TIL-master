import sys
sys.stdin = open('4195.txt', 'r')

def parent_field(x):
    if x == parent[x]:
        return x
    else:
        p = parent_field(parent[x])
        parent[x] = p
        return parent[x]

def union(x,y): #합쳐주는 함수
    x = parent_field(x)
    y = parent_field(y)
    #두사람이 친구가 아닌 경우 연결
    # y를 parent로 x를 연결하고 x의 친구관계숫자에 y가 가진 친구 수 더한다.
    if x != y:
        parent[y] = x
        number[x] += number[y]

tc = int(input())

for _ in range(tc):
    n = int(input())
    parent, number = dict(), dict()
    for _ in range(n):
        print(parent)
        x, y = input().split()
        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1
        union(x, y)
        print(number[parent_field(x)])
