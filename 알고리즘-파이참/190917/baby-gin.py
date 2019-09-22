# 124783 667767 054060 101123

def run(ls, num, n): # 112233 과 같은 경우 안된다.
    # for i in range(len(ls)):
    #     if
    if n == 4:
        return'Nothing'
    if ls[0] == ls[1] == ls[2]:
        num += 1
        for i in range(3):
            ls.pop(0)
    n += 1
    if ls != []:
        return triplete(ls, num, n)
    if num == 2:
        return 'Baby-gin'

def triplete(ls, num, n):
    if ls[0] == ls[1] -1 and ls[0] == ls[2] -2:
        num += 1
        for i in range(3):
            ls.pop(0)
    n += 1
    if ls != []:
        return run(ls, num, n)
    if num == 2:
        return 'baby-gin'

ls = list(map(int, input().split()))
ls.sort()
print(run(ls, 0, 0))
