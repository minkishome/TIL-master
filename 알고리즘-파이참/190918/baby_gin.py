import sys
sys.stdin = open('baby_gin.txt', 'r')

def run1(ls): # 모든 조건
    for i in ls:
        if ls.count(i) >= 3:
            return 1
    else:
        return 0



def triplet(ls):
    for i in range(0,len(ls)-1):
        if ls[i]+1 in ls and ls[i]+2 in ls:
            return 1
        elif ls[i]-1 in ls and ls[i]+1 in ls:
            return 1
        elif ls[i]-2 in ls and ls[i]-1 in ls:
            return 1
    else:
        return 0


for tc in range(1, int(input()) + 1):
    ls = list(map(int,input().split()))
    # 하나씩 받는다
    cnt_a, cnt_b = 0, 0
    card_a = []
    card_b = []
    for i in range(len(ls)):
        if i % 2 == 0: # A가 카드를 받을 상황
            card_a.append(ls[i])
            if i >= 4:
                cnt_a += run1(card_a)
                cnt_a += triplet(card_a)
                if cnt_a != 0:
                    print('#%d 1' %(tc))
                    break
        else: # B가 카드를 받을 상황
            card_b.append(ls[i])
            if i >= 5:
                cnt_b += run1(card_b)
                cnt_b += triplet(card_b)
                if cnt_b != 0:
                    print('#%d 2' %(tc))
                    break
    if cnt_a == 0 and cnt_b == 0:
        print('#%d 0' %(tc))