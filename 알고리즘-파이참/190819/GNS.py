import sys

sys.stdin = open('GNS.txt','r')
# ts = int(input())

#
# for i in range(ts):
#     num, task_case = input().split()
#     task = list(map(str,input().split()))
#     new_list = []
#     new_num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
#     while not len(task) == len(new_list):
#         for a in new_num:
#             count = 0
#             for b in task:
#                 if a == b:
#                     count += 1
#             new_list += [a]*count
#
#     print('%s' %(num))
#     print(' '.join(new_list))

def atoi(a):
    num_dict = {"ZRO" : 0, "ONE" : 1, "TWO" : 2, "THR" :3, "FOR" :4
                   , "FIV" : 5, "SIX" : 6, "SVN" : 7, "EGT" : 8, "NIN" : 9}
    return num_dict[a]

def itoa(b):
    num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    return num_list[b]

for _ in range(int(input())):
    tc = input().split()
    case = map(atoi, input().split())
    print(tc[0])
    result = map(itoa, sorted(case))
    print(' '.join(result))
