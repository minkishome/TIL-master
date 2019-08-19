import sys

sys.stdin = open('4839.txt','r')

def check_page(lp,rp,cp):
    count = 0
    while 1:
        mp = int((lp + rp)/2)
        if mp == cp:
            break
        if mp > cp:
            rp = mp
        elif mp < cp:
            lp = mp
        count+= 1
    return count

tc = int(input())
for test_num in range(tc):
    problem = list(map(int,input().split()))
    page_total = problem[0]
    Pa = problem[1]
    Pb = problem[2]
    A_page = check_page(1,page_total,Pa)
    B_page = check_page(1,page_total,Pb)
    if A_page > B_page:
        print('#%d B' %(test_num+1))
    elif B_page >A_page:
        print('#%d A' % (test_num + 1))
    elif A_page == B_page:
        print('#%d 0' % (test_num + 1))
