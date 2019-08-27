import sys
sys.stdin = open('4880.txt', 'r')
#
# def rsp(a, b): # 가위바위보 함수
#     pass

def half(ls1, ls2): #나눌 함수(ls1)와 나눈 함수를 더할 곳 ls2 ls2의 각 인자가 2이하가 아닐 경우 계속해서 반복
    for i in ls1:
        if len(i) > 2:
            a = ls1.pop()
            ls1.append(a[:len(ls1)//2+1])
            ls1.append(a[len(ls1)//2+1:len(ls1)])

    # 나누는 위치는 (len(ls1)//2)
    # if len(ls1) > 2:
    #     a = ls1[:len(ls1)//2+1]
    #     if len(a) > 2:
    #         return half(a,ls2)
    #     else:
    #         ls2.append(a)
    #     b = ls1[len(ls1)//2+1:len(ls1)]
    #     if len(b) > 2:
    #         return half(a,ls2)
    #     else:
    #         ls2.append(b)
    #     return ls2
    # else:
    #     ls2.append(ls1)


test_num = int(input())

for tc in range(test_num):
    people_num = int(input())
    game_list2 = [0] * people_num
    game_list = list(map(int,input().split()))
    for t in enumerate(game_list):
        game_list2[t[0]] = t
    game_list2 = [game_list2]
    print(game_list2)
    game_list_split = []
    print(half(game_list2,game_list_split))
