import sys
sys.stdin = open('cardcard.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    card = list(input())
    cards = [0] * (len(card) // 3)
    cards_ = set()
    S_count = D_count = H_count = C_count = 13
    a = 0
    count = 0
    for i in range(len(card) // 3):
        cards_.add(card[3 * i] + card[3 * i + 1] + card[3 * i + 2])
        count += 1

    if len(cards_) != count:
        print('#{} ERROR'.format(test_case))
    else:
        for j in cards_:
            if 'S' in j:
                S_count -= 1
            elif 'D' in j:
                D_count -= 1
            elif 'H' in j:
                H_count -= 1
            elif 'C' in j:
                C_count -= 1

        print('#{} {} {} {} {}'.format(test_case, S_count, D_count, H_count, C_count))
