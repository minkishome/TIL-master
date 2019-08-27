import sys
sys.stdin = open('작업순서.txt', 'r')



for _ in range(11):
    N, M = map(int, input().split())
    ls = list(map(int, input().split()))

    path_dict = {}
    for i in range(len(ls)//2): # 1딕셔너리?
        if not ls[2*i] in path_dict.keys():
            path_dict[ls[2*i]] = [ls[2*i+1]]
        else:
            path_dict[2 * i]
    print(path_dict)

