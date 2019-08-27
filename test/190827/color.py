import sys
sys.stdin = open('color.txt', 'r')

test_num = int(input())

for tc in range(1,test_num+1):
    info = list(map(int,input().split())) # info[0] = N info[1] = M info[2] = k(색칠 반복수
    matrix = [[0]* info[1] for _ in range(info[0])]
    a = [0]* info[2]
    col = set()
    for test in range(info[2]):
        a[test] = list(map(int,input().split()))
        col.add(a[test][4])
    col.add(0)
    for k in range(len(a)):
        for i in range(a[k][0], a[k][2] +1):
            for j in range(a[k][1], a[k][3] + 1):
                if matrix[i][j] < a[k][4]:
                    matrix[i][j] = a[k][4]
                elif matrix[i][j] >= a[k][4]:
                    pass

    color_dict = {}
    for l in col:
        result = 0
        b = 0
        for ls in matrix: # l 값으로 딕셔너리 만들고 전체 카운트를 해준다.
            b += ls.count(l)
        color_dict[l] = b
    # print(color_dict)
    print('#%d %d'%(tc,max(color_dict.values())))


    #             elif matrix[i][j] == a[k][4]:
    #
    #             else:
    #                 if matrix[i][j] > a[k][4]: # 기존의 값이 새로운 명도보다 높은 경우 만약 색칠한 경우가 있다면 0으로 중복방지를 위해 내가 걸어온 좌표를 전부 체크?
    #                     if matrix[i][j] != 0:
    #                         # for z in ls_find:
    #                         #     matrix[z[0]][z[1]] = 0
    #                         for u in range(a[k][0], a[k][2] + 1):
    #                             for s in range(a[k][1], a[k][3] + 1):
    #                                 if matrix[u][s] == a[k][4] and matrix[u][s] == 0:
    #                                     matrix[u][s] = 0
    #                         # for z in ls_find:
    #                         #     matrix[z[0]][z[1]] = 0
    #                         break
    #                 else: # 색이 낮으면 색칠 안하고 높으면 덮어 씌운다.
    #                     for u in range(info[0]):
    #                         for s in range(info[1]):
    #                             if matrix[u][s] == k:
    #                                 matrix[u][s] = 0
    #                         matrix[i][j] = a[k][4]
    # print(matrix)
