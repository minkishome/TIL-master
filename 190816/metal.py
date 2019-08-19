import sys

sys.stdin = open('metal.txt','r')
tc = int(input())
for test_num in range(tc):
    num = int(input())
    ls = list(map(int,input().split()))
    ls_tu = []
    while 1:
        ls_tu.append((ls[0],ls[1]))
        ls.pop(0)
        ls.pop(0)
        if len(ls) == 0:
            break


    count = 0
    ls_final = []

    first = ()
    for i in ls_tu:
        count = 0
        for j in ls_tu:
            if i[0] == j[1]:
                count += 1
        if count == 0:
            first = i
    ls_final.append(first)


    while 1:
        for z in ls_tu:
            if ls_final[-1][1] == z[0]:
                ls_final.append(z)
        if len(ls_final) == len(ls_tu):
            break


    ls_str = ''
    for i in ls_final:
        for j in range(2):
            ls_str += ' '+ str(i[j])
    print('#%d%s'%(test_num+1,ls_str))





    # z = 1
    # while z:
    #      for i in range(1,n - 2):
    #          back = ls_tu[i][1]
    #          for j in range(i+1, n-1):
    #              if back == ls_tu[j][0]:
    #                  ls[i+1] = ls_tu[j]
    #
    #      while 1:
    #         a = 0
    #         if ls_tu[a][1] == ls_tu[a+1][0]:
    #             z = 0
    #             break
    #         else:
    #             for i in range(1, n - 1):
    #                 forward = ls_tu[i][0]
    #                 for j in range(i + 1, n):
    #                     if forward == ls_tu[j][1]:
    #                         ls_tu.insert(i,ls_tu[j])
    #             z = 0
    #             break
    #         a += 1
    #
    # print(ls_tu)
