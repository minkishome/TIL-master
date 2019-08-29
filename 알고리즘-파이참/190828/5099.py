import sys
sys.stdin = open('5099.txt','r')

test_num = int(input())

for tc in range(test_num):
    info = tuple(map(int, input().split()))
    fire = list(map(int, input().split()))
    fire2 = [0] * len(fire)
    for i in range(len(fire)):
        fire2[i] = tuple(fire[0], i+1)
    print(fire2)
    # info[0] = 화덕의 크기 info[1] = 피자의 개수

