import itertools

def make_point():
    return

def make_lineup(ls, z):
    if z == 9:
        return make_point()
    else:
        for i in range(1, 9):
            check[i] = True
            if i == 4:
                continue
            ls_lineup[i] = ls_hit[i] 



N = int(input())
ls_hit = [list(map(int, input().split()) for _ in range(N)]
max_point = 0
ls_base = [0,0,0,0] # 앞에서 부터 타석, 1,2,3
ls_lineup = [0,0,0,0,0,0,0,0,0] # 타석 순서 0~8
check = [False] * 9
ls_lineup[3] = ls_hit[0] # 1번타자 4번으로 지정

