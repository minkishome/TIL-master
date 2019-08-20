import sys
sys.stdin = open('flatten.txt','r')


for tc in range(1, 11):
    count_num = int(input())
    building_list = list(map(int,input().split()))
    for i in range(count_num):
        a = max(building_list)
        b = min(building_list)
        building_list.remove(a)
        building_list.remove(b)
        building_list.append(a-1)
        building_list.append(b+1)
    a = max(building_list)
    b = min(building_list)
    last_num = a-b
    print('#%d %d ' %(tc, last_num))