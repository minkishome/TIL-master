# def selectionsort(ls, n, i):
#     if i == n-1:
#         return ls
#     min_val = i
#     for j in range(i+1, n):
#         if ls[j] < ls[min_val]:
#             min_val = j
#     ls[i], ls[min_val] = ls[min_val], ls[i]
#     return selectionsort(ls, n, i+1)
#
#
#
# ls = [9,4,6,8,78,1,3,5]
#
# print(selectionsort(ls, 8, 0))

ls = [-1, 3, -9, 6, 7, -4, 1, 5, 4, -2]
# n = len(ls)
# cnt = 0
# for i in range(0, (1<<n)):
#     ls2 =[]
#     for j in range(0, n):
#         if i & (1<<j):
#             # print('%d '%ls[j], end ='')
#             ls2.append(ls[j])
#     if sum(ls2) == 0 and ls2 != []:
#         print(ls2)
#         cnt += 1
# print(cnt)


def make_part(ls, z):
    global n

    for i in range(0, n):
        if not visited[i]:
            visited[i] = True
            ls2.append(ls[i])
            if sum(ls2) == 0:
                print(ls2)
            make_part(ls, z+1)
            visited[i] = False
    return
ls2 = []
n = len(ls)
visited = [False] * (len(ls)+1)
make_part(ls, 0)