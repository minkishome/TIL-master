import sys
sys.stdin = open('contact.txt', 'r')






for z in range(10):
    n,m = map(int, input().split()) # m이 시작점
    ls = list(map(int, input().split()))
    path_dict = {}
    for i in range(len(ls)//2):
        if not ls[2*i] in path_dict.keys():
            path_dict[ls[2*i]] = [ls[2*i + 1]]
        else:
            path_dict[ls[2 * i]] += [ls[2 * i + 1]]
    print(path_dict)
    a = path_dict[m]
    stack = []  # 찾아갈 친구들이 append
    stack2 = []
    que = set()
    que2 = []
    for i in a:
        stack.append(i)
        que.add(i)
        que2.append(i)
    while que:
        for i in range(len(que)):
            b = que.pop()
            if not i in que2:
                stack2.append(b)
        print(stack2)
        for i in stack2:
            if path_dict[i] != []:
                for j in path_dict[i]:
                    que.add(j)
        stack.append(stack2)
        stack2 = []
    print(stack)
    print(stack[-1])
