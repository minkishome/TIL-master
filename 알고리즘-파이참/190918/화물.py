import sys
sys.stdin = open('화물.txt', 'r')


def find(ls): # pop하고 append, len이 같으면 그만 => 더 이상 추가할것이 없다는 얘기니깐
    for i in ls:
        


for tc in range(1, int(input())+1):
    n = int(input())
    ls = [list(map(int, input().split())) for _ in range(n)]
    a = ls[0]
    for i in ls:
        if i[1] < a[1]:
            a = i
    ls2 = [a]
