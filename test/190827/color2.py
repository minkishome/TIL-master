import sys
sys.stdin = open('color.txt', 'r')

test_num = int(input())

for tc in range(1,test_num+1):
    info = list(map(int,input().split())) # info[0] = N info[1] = M info[2] = k(색칠 반복수
    matrix = [[0]* info[1] for _ in range(info[0])]
    a = [0]* info[2]
    col = []
    for test in range(info[2]):
        a[test] = list(map(int,input().split()))
        col.append(a[test][4])
    col.append(0)
    for k in range(len(a)): # a의 각 색깔에 따라
        ls_find = []
        for i in range(a[k][0], a[k][2] +1):
            for j in range(a[k][1], a[k][3]+1):
                ls_find.append((i,j))
        some = 0
        for z in ls_find:
           if matrix[z[0]][z[1]] > a[k][4]:
               some += 1
        if some != 0: # 아무것도 하지 않겠다. 하나라도 큰게 있는 경우
            pass
        else:
            for z in ls_find:
                matrix[z[0]][z[1]] = a[k][4]

    color_dict = {}
    for l in col:
        result = 0
        b = 0
        for ls in matrix: # l 값으로 딕셔너리 만들고 전체 카운트를 해준다.
            b += ls.count(l)
        color_dict[l] = b
    print(color_dict)
    print('#%d %d'%(tc,max(color_dict.values())))