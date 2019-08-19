import sys
sys.stdin = open('4834.txt','r')

T = int(input())
for tc in range(1, T+1):
    counting = int(input())
    card_input = int(input())
    ls_index = []
    card = [0] * 10
    for i in range(counting):
        a = card_input % 10
        card[a] += 1
        card_input = card_input//10

    #card list 생성
    maxidx = 0
    for i in range(len(card)):
        if card[i] >= card[maxidx]:
            maxidx = i



    print('#%d %d %d' %(tc ,maxidx , card[maxidx]))
