import sys
sys.stdin = open('5174.txt', 'r')

for tc in range(int(input())):
    E, N = map(int, input().split())
    ls = list(map(int, input().split()))
    ls_dict = {ls[2*i] : []  for i in  range(len(ls)//2)}
    for i in range(len(ls)//2):
        ls_dict[ls[2*i]] += [ls[2*i +1]]
    # print(ls_dict)
    que = []
    if N in ls_dict.keys():
        for i in ls_dict[N]:
            que.append(i)
        count = 1
        # print(que)
        while que:
            count += 1
            a = que.pop()

            if a in ls_dict.keys():
                for i in ls_dict[a]:
                    que.append(i)


        print('#%d %d' %(tc+1, count))
    else:
        print('#%d %d' %(tc+1, 1))