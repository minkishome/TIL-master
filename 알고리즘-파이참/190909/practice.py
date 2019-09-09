import sys
sys.stdin = open('sample.txt', 'r')

def find():
    while que:
        b = que.pop(-1)
        if b in dict_node.keys():
            a = dict_node[b]
            for z in a:
                que.append(z)
                ls_point.append(z)
                find()
    return

N = int(input())
ls = list(map(int, input().split()))



dict_node = {ls[i*2] : [] for i in range(len(ls)//2) }

for i in range(len(ls)//2):
    dict_node[ls[2*i]] += [ls[2*i+1]]







print(dict_node)
que = [1]
ls_point = [1]
find()





# while que:
#     b = que.pop(-1)
#     if b in dict_node.keys():
#         a = dict_node[b]
#         for z in a:
#             que.append(z)
#             ls_point.append(z)
#     else:
#         pass
    # if len(ls_point) == N:
    #     break
print(ls_point)
