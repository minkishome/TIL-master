import sys

sys.stdin = open('4843.txt','r')

tc = int(input())
for test_num in range(tc):
    num = int(input())
    num_in_list= list(map(int,input().split()))
    n = len(num_in_list)
    empty_list = [0]*10
    # 선택 정렬을 통한 오름차순 정리
    for i in range(0,n-1):
        min = i
        for j in range(i+1,n):
            if num_in_list[j] < num_in_list[min]:
                min = j
        num_in_list[i], num_in_list[min] = num_in_list[min], num_in_list[i]
    count = 0
    while count < 9:
        empty_list[count] = num_in_list[-1]
        empty_list[count+1] = num_in_list[0]
        num_in_list.pop(0)
        num_in_list.pop(-1)
        count += 2
    empty_list = ' '.join(map(str, empty_list))
    print('#%d %s' %(test_num+1,empty_list))
