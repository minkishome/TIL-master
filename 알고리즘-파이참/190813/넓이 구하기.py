# 1 2 4 4
# 2 3 5 7
# 3 1 6 5
# 7 3 8 6
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
D = list(map(int,input().split()))

def make_area(ls1, ls2, ls3, ls4):
    A1 = ls1[2] - ls1[0]
    B1 = ls1[3] - ls1[1]
    A2 = ls2[2] - ls2[0]
    B2 = ls2[3] - ls2[1]
    A3 = ls3[2] - ls3[0]
    B3 = ls3[3] - ls3[1]
    A4 = ls4[2] - ls4[0]
    B4 = ls4[3] - ls4[1]
    # 각 사각형의 길이를 구헀다.
    area1 = A1*B1 + A2*B2 + A3*B3 + A4*B4 # 각자의 넓이를 구하고
    return area1
    #겹치는 부분을 구하자


    # 겹치는 부분을 리스트로 만들어 주자

def share_area(ls1,ls2):
    x1,x2,y1,y2 = [],[],[],[]
    for i in range(ls1[0], ls1[2]+1):
        x1.append(i)
    for i in range(ls2[0], ls2[2]+1):
        x2.append(i)
    for i in range(ls1[1], ls1[3] + 1):
        y1.append(i)
    for i in range(ls2[1], ls2[3] + 1):
        y2.append(i)
    ls_share_x = list(set(x1).intersection(x2))
    ls_share_y = list(set(x2).intersection(y2))
    if ls_share_x == [] or ls_share_y ==[]:
        return 0
    else:
        ls_share_new = [ls_share_x[0],ls_share_y[0],ls_share_x[-1],ls_share_y[-1]]
        return (ls_share_new[2]-ls_share_new[0])*(ls_share_new[3]-ls_share_new[0])






# 겹치는 구간 잘못 구함

print(make_area(A,B,C,D)-share_area(A,B)-share_area(A,C)-share_area(A,D)-share_area(B,C)-share_area(B,D)-share_area(C,D) )