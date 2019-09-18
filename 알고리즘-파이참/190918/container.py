import sys
sys.stdin = open('container.txt', 'r')

def find(ls_con, ls_bus):
    summ = 0
    cnt = 0
    a = min(len(ls_bus), len(ls_con))
    for i in range(len(ls_con) -1 , -1, -1):
        cnt += 1
        for j in range(len(ls_bus) -1, -1, -1):
            if ls_con[i] <= ls_bus[j]:
                summ += ls_con[i]
                ls_bus[j] = 0
                break

        if cnt == a:
            return summ










for tc in range(int(input())):
    N, M = map(int, input().split())
    ls_con = list(map(int, input().split()))
    ls_con.sort()
    ls_bus = list(map(int, input().split()))
    ls_bus.sort()



    b = find(ls_con, ls_bus)
    print('#%d %d' %(tc+1, b))