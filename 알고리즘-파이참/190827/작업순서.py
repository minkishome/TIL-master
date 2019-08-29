import sys
sys.stdin = open('작업순서.txt', 'r')



for z in range(10):
    info = tuple(map(int, input().split()))
    ls = list(map(int, input().split()))
    ls_idx = [0] * info[0] # 각 숫자가 몇번 나왔는지를 확인
    ls_count = [0] * info[0] # 노드의 갯수를 체크해주는 것 이것과 ls_idx가 같을때 탐색할 수 있다.
    path_dict = {i : [] for i in range(1,info[0]+1)}
    ls_find = [0] * info[0] # value에 들어있지 않은 숫자가 시작점이 되므로 이를 확인하기 위함
    que = []
    stack = []

    for i in range(len(ls)//2): # 1딕셔너리?
        path_dict[ls[2*i]] += [ls[2*i+1]]
    # print(path_dict)
    print(path_dict)
    for num in path_dict.values():
        for i in num:
            if ls_find[i-1] == 0:
                ls_find[i-1] = i
    # print(ls_find) # i-1의 위치가 없는 놈이 시작점이 된다.
    for i in path_dict.keys():
        if i not in ls_find:
            que.append(i) # 시작점을 만들어주고
    # 몇번 나오는지를 체크해야한다.
    for j in path_dict.values():
        for i in j:
            ls_idx[i-1] += 1
    # print(ls_idx) # 몇번 나와야하는지 체크됨
    while que:
        a = que.pop(0)
        stack.append(a)
        # que에서 뽑은 값을 딕셔너리에 대입해서 몇번 나왔는지 체크, 그러고 나서 ls_idx의 값과 같을때 que에 넣을 수 있도록
        b = path_dict[a]
        for i in b:
            ls_count[i-1] += 1 # 나온 횟수 체크
        for i in b:
            if ls_idx[i-1] == ls_count[i-1]:
                que.append(i)\

    print('#%d' %(z), end = ' ')
    for i in stack:
        print(i , end= ' ')
    print()