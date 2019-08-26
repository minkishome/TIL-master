import sys

sys.stdin = open('2116.txt', 'r')

num = int(input())

dice = [[0] for _ in range(num)]

for i in range(num):
    a = list(map(int,input().split()))
    dice[i] = a
dice_sum = [0] * 6

dice_couple = {
    0 : 5, 5: 0,
    1 : 3, 3: 1,
    2 : 4, 4 : 2
}



sum_list = []

for i in dice[0]:
    number = dice[0].index(i) # 제일 밑에 깔리는 숫자의 인덱스
    counting = 0
    dice_num = 0
    summ = 0
    while 1:
        a = dice_couple[number] # 반대편 숫자의 인덱스 위치, 이게 다음 주사위의 밑에 깔리는 숫자가 된다.
        summ += sum(dice[dice_num]) - dice[dice_num][a] - dice[dice_num][number]
        counting += 1

        dice_num += 1
        if dice_num == num:
            break
        number = dice[dice_num].index(dice[dice_num-1][a])
    sum_list.append(summ)

print(max(sum_list)) # 각 위아래 숫자를 뺀 뒤 각 면의 최대 값을 구한뒤 더해주면 된다.



