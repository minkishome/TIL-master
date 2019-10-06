import sys, copy
sys.stdin = open('max.txt', 'r')

def change_num(ls, ls2, i, cnt):



for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    ls = []
    for i in str(N):
        ls.append(int(i))
    ls2 = copy.deepcopy(ls)
    ls2.sort()
    ls2.reverse()




#1 321
#2 7732
#3 857147
#4 87664
#5 88832
#6 777770
#7 966354
#8 954311
#9 332211
#10 987645