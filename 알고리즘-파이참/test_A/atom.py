import sys
sys.stdin = open('atom.txt', 'r')

for test_num in range(int(input())):
    N = int(input())
    ls = [0] * N
    ls1 = [0] * N
    for z in range(N):
        ls[z] = list(map(int,input().split()))
    print(ls)
    apower = 0
    for i in range(len(ls1)-1): #i[0] = x i[1] = y i[2] = 방향 i[3] = 에너지
        for j in range(i+1,len(ls1)):
            #일단은 같은 y축에 대해 x 이동만 확인 -> y는 유사하니깐
            if ls[i] !=0 and ls[j] !=0:
                if ls[i][1] == ls[j][1]:
                    if ls[i][1] < ls[j][1]:
                        a = ls[i][1]
                        if ls[i][2] == 3 and ls[j][2] == 2: # 만나서 터지는 점
                            apower+= ls[i][3]+ ls[j][3]
                            ls[i] = 0
                            ls[j] = 0

                            b = (ls[i][0] + ls[j][0])/2
                            for z in range(len(ls1)):
                                if ls[z][1] == a + b:
                                    apower += ls[z][3]
                                    ls[z] = 0
                    if ls[i][1] > ls[j][1]:
                        a = ls[i][1]
                        if ls[i][2] == 2 and ls[j][2] == 3: # 만나서 터지는 점
                            apower+= ls[i][3]+ ls[j][3]
                            ls[i] = 0
                            ls[j] = 0

                            b = (ls[i][0] + ls[j][0])/2
                            for z in range(ls):
                                if ls[z][1] == a + b:
                                    apower += ls[z][3]
                                    ls[z] = 0
                if ls[i][0] == ls[j][0]:
                    if ls[i][0] < ls[j][0]:
                        a = ls[i][0]
                        if ls[i][2] == 0 and ls[j][2] == 1: # 만나서 터지는 점
                            apower+= ls[i][3]+ ls[j][3]
                            ls[i] = 0
                            ls[j] = 0
                            for z in range(len(ls1)):
                                if ls[z][0] == a + b:
                                    apower += ls[z][3]
                                    ls[z] = 0
                    if ls[i][0] > ls[j][0]:
                        a = ls[i][0] #///// 바꿔라
                        if ls[i][2] == 1 and ls[j][2] == 0: # 만나서 터지는 점
                            apower+= ls[i][3]+ ls[j][3]
                            ls[i] = 0
                            ls[j] = 0
                            b = (ls[i][0] + ls[j][0])/2
                            for z in range(len(ls1)):
                                if ls[z][0] == a + b:
                                    apower += ls[z][3]
                                    ls[z] = 0
    print(apower)