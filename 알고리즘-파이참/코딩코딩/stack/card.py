N = int(input())
ls_card = [0] * N
a = 0

for i in range(N, 0, -1):
    ls_card[a] = i
    a += 1

while len(ls_card) != 1:
    ls_card.pop(-1)
    print(ls_card)
    ls_card2 = [0] * len(ls_card)
    b = ls_card[-1]
    for i in range(len(ls_card) - 1):
        ls_card2[i+1] = ls_card[i]
    ls_card2[0] = b
    print(ls_card2)

print(ls_card[0])