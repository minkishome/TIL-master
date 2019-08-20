import sys
sys.stdin = open('4837.txt','r')



tc = int(input())
num_list = [1,2,3,4,5,6,7,8,9,10,11,12]
n = len(num_list)
part_num_list = []
for i in range(tc):
    b , c = map(int,input().split())
    count = 0
    for h in range(1, 1 << n):
        part_part = []
        for j in range(n + 1):
            if h & (1 << j):
                part_part.append(num_list[j])
        if len(part_part) > b:
            part_num_list.append(part_part)
            # for i in range(1, 1 << n):
            #     part_part = []
            #     for j in range(n + 1):
            #         if i & (1 << j):
            #             part_part.append(num_list[j])
            #     if len(part_part) >
            #         part_num_list[i - 1] = part_part

    for alpha in part_num_list:
        if sum(alpha) == c:
            count += 1
    print('#%d %d' %(i+1, count))



# num_list = [1,2,3,4,5,6,7,8,9,10,11,12]
# n = len(num_list)
# part_num_list = [0]*(2**12-1)
#
# for i in range(1,1<<n):
#     part_part = []
#     for j in range(n+1):
#         if i & (1 << j):
#             part_part.append(num_list[j])
#     part_num_list[i-1] = part_part
#
#
# # part_num_list라는 리스트에 num_list의 모든 부분집합을 넣음
#
# tc = int(input())
# for i in range(tc):
#     b , c = map(int,input().split())
#     count = 0
#     for j in part_num_list:
#         if len(j) == b and sum(j) == c:
#             count += 1
#     print('#%d %d' %(i+1, count))

