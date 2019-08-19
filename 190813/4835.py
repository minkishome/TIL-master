import sys
sys.stdin = open('4835.txt','r')


T = int(input())
for tc in range(1, T+1):
    list_len = list(map(int, input().split()))
    original_list = list(map(int, input().split()))
    slice_num = list_len[1]
    list_len_int = list_len[0] - list_len[1]
    num =list_len_int + 1
    sum_list = [0] * num

    for i in range(num):
        sum_list[i] = sum(original_list[i:i + slice_num])
    result = max(sum_list) - min(sum_list)
    print('#%d %d'%(tc, result))

