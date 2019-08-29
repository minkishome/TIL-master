import sys, copy
sys.stdin = open('card.txt', 'r')

def x0(ls):
    ls1 = ls[0:(len(ls)//2)]
    ls2 = ls[(len(ls)//2):len(ls)]

    # 슬라이싱을 통해 나눔
    ls = ls2[::-1] + ls1
    return ls




def x1(ls):
    ls1 = ls[0:(len(ls) // 2)]
    ls2 = ls[(len(ls) // 2):len(ls)]


    pass


def x2(ls):
    ls1 = ls[0:(len(ls) // 2)]
    ls2 = ls[(len(ls) // 2):len(ls)]
    pass
def x3(ls): # == x2
    ls1 = ls[0:(len(ls) // 2)]
    ls2 = ls[(len(ls) // 2):len(ls)]
    pass


def x4(ls): # == x1
    ls1 = ls[0:(len(ls) // 2)]
    ls2 = ls[(len(ls) // 2):len(ls)]
    pass


def x5(ls): # == x0
    ls1 = ls[0:(len(ls) // 2)]
    ls2 = ls[(len(ls) // 2):len(ls)]
    # 슬라이싱을 통해 나눔
    ls = ls1 = ls2
    pass

test_num = int(input())

for tc in range(test_num):
    N = int(input())
    ls_original = list(map(int, input().split()))
    ls_chan = copy.deepcopy(ls_original)
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if ls_original[min_idx] > ls_original[j]:
                min_idx = j
        ls_original[i], ls_original[min_idx] = ls_original[min_idx], ls_original[i] # 마지막에 정렬이 제대로 되었는지를 확인
    print(ls_chan[::-1])
