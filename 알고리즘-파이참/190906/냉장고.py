import sys, itertools
sys.stdin = open('냉장고.txt', 'r')

def calc (a,b): # a,b는 두개의 숫자를 가진 리스트
    ax, ay = a
    bx, by = b
    return abs(ax-bx) + abs(ay-by)

def gohome(new_x, ksum, depth):
    global minsum

    if depth == n:
        ksum += calc(new_x, end) # 그 자리에서 바로 가지치기
        if minsum > ksum:
            minsum = ksum
    else: #아직 원하는 값이 나오지 않았을때
        for i in range(2, n+2): #처음 두개는 집, 회사
            if not visited[i]:
                new_sum = ksum + calc(new_x, case[i]) # 새롭게 붙을 순열의 값을 더해준다.
                visited[i] = True #한번 들어간거 새로 들어가면 안됨
                gohome(case[i], new_sum, depth+1)
                visited[i] = False



for tc in range(1, int(input())+1):
    n = int(input())
    a = list(map(int, input().split()))
    visited = [False] * (n+3)
    case = []
    for i in range(n+2):
        case.append((a[2*i], a[2*i+1]))
    start = case[0]
    end = case[1]
    minsum = 999999999
    gohome(start, 0, 0)
    print('#%d %d' % (tc, minsum))
