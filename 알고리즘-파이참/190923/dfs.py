import copy

def dfs1(v): # 재귀함수!
    visited[v] = 1
    print(v, end = ' ')
    for w in edges[v]:
        if not visited[w]:
            dfs1(w)

def dfs2(v):
    s = []
    s.append(v)
    while s:
        v = s.pop(-1)
        if not visited[v]:
            visited[v] = 1
            print(v, end= ' ')
            for w in edges[v]:
                if not visited[w]:
                    s.append(w)

tin = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]
edges = [[] for i in range(8)]
n = len(tin)//2
visited =[0]*(n+1)
dfs1(1)
# ls = [[1,2],[1,3],[2,4],[2,5],[4,6],[5,6],[6,7],[3,7]]
# n = len(ls)
# check = [False] * (n+1)
# que = [1]
#
# for i in range(n):
#     if not check[i]:
#         check[i] = True
#