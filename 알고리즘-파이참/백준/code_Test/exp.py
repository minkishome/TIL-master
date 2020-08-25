# from collections import deque as dq
#
# def solution(food_times, k):
#     food_times = dq([(food, idx) for idx, food in enumerate(food_times, 1)])
#     print(food_times)
#     food_times = dq(sorted(food_times, key=lambda x: x[0]))
#     print(food_times)
#     small_food = food_times[0][0]
#     prev_food = 0
#     while k - ((small_food - prev_food) * len(food_times)) >= 0:
#         # 해당 음식을 완전히 소비하는 데 걸린 시간만큼 뺀다
#         k -= (small_food - prev_food) * len(food_times)
#
#         prev_food, index = food_times.popleft()
#         if not food_times:
#             return -1
#         small_food = food_times[0][0]
#     food_times = sorted(food_times, key=lambda x: x[1])
#     return food_times[k % len(food_times)][1]
# print(solution([3,1,2], 5 ))


node = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
max_y =max(node,key=lambda x :x[1])

print(max_y)

# class Tree:
#     def __init_(self, datalist):
#         self.data = max(datalist, key = lambda x : x[1])
#         leftlist = list(filter(lambda x :x[0] < self.data[0]), datalist)
#         rightlist = list(filter(lambda x :x[0] < self.data[0]), datalist)
#
#         if leftlist != []:
#             self.left = Tree(leftlist)
#         else:
#             self.left = None
#         if rightlist != []:
#             self.right = Tree(rightlist)
#         else:
#             self.right -




class Tree:
    def __init__(self, datalist):
        self.data = max(datalist, key=lambda x:x[1])
        # 가장 큰값의 x[0]보다 왼편
        leftlist = list(filter(lambda x:x[0] < self.data, datalist))
        rightlist = list(filter(lambda x:x[0] > self.data, datalist))

        if leftlist != []:
            self.left = Tree(leftlist)
        else:
            self.left = None

        if rightlist != []:
            self.right = Tree(rightlist)
        else:
            self.right = None

def fix(node, postlist, prelist):
    postlist.append(node.data)
    if node.left is not None:
        fix(node.left, postlist, prelist)
    if node.right is not None:
        fix(node.right, postlist, prelist)
    prelist.append(node.data)