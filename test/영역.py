import sys
sys.stdin = open('test1.txt', 'r')

test_case = int(input())



for tc in range(test_case):
    info = list(map(int, input().split())) # info[0] = N의 크기 info[1] = 겹치는 영역의 수
    N = info[0]
    M = info[1]
    count_set = set()
    info_list = []
    for i in range(M):
        a = list(map(int, input().split())) # 좌표값 설정 받음
        info_list.append(a)
    for a in info_list:
        for x in range(a[0], a[2]+1):
            for y in range(a[1], a[3]+1):
                count_set.add((x,y))
    print('#%d %d' %(tc+1, len(count_set)))
