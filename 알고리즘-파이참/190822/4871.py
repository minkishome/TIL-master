import sys
sys.stdin = open('4871.txt', 'r')
# 1 4
# 1 3
# 2 3
# 2 5
# 4 6

def solve_way(ls, start, end):
    qu = [] # 앞으로 처리해야할 이동 경로
    done = set() #이미 이동한 경로( 여기선 필요없음)

    qu.append(start)
    done.add(start)

    while qu:
        p = qu.pop(0)
        v = p
        if v == end:
            return 1
        for x in ls:
            if p == x[0]:
                qu.append(x[1])
                done.add(x[1])

    return 0


test_num = int(input())
for tc in range(test_num):
    info = list(map(int, input().split()))
    way_list = [0] * info[1]
    for i in range(info[1]):
        way_list[i] = list(map(int, input().split()))
    destination = list(map(int,input().split()))
    print('#%d %d'%(tc+1,solve_way(way_list, destination[0], destination[1])))