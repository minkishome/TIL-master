my = [1, 2, 3, 4, 5, 6]

real = [1, 2, 3, 4, 5, 7]
bonus = 6

# my와 real의 6개가 같으면 1등
# my와 real이 다섯개가 같고, 나머지 하나가 bonus면 2등
# my와 real이 5개가 같으면 3등
# ''4개가 같으면 4등
# '' 3개가 같으면 5등
# 나머지는 꽝
numbers = []

for i in real:
    if i in my:
        numbers .append(i)

if len(numbers) > 5:
    print('1등')
elif len(numbers) > 4:
    if 6 in my:
        print('2등')
    else:
        print('3등')
elif len(numbers) > 3:
    print('4등')
elif len(numbers) > 2:
    print('5등')
else:
    print('꽝')
