from  itertools import permutations


N = int(input())
ls_hit = [list(map(int, input().split())) for _ in range(N)]
max_point = 0


for i in permutations(range(1,9)):
    turn = i[:3] + (0, ) + i[3:]
    score = 0
    player_num = 0
    for inn in range(N):
        p1, p2 ,p3 = 0, 0, 0
        out_num = 0
        while out_num != 3:
            hitter = ls_hit[inn][turn[player_num]]
            if hitter == 0:
                out_num += 1
            elif hitter == 1:
                score += p3
                p1, p2, p3 = 1, p1, p2
            elif hitter == 2:
                score += p2 + p3
                p1, p2, p3 = 0, 1, p1
            elif hitter == 3:
                score += p1 + p2 + p3
                p1, p2, p3 = 0, 0, 1
            # elif hitter == 4:
            else:
                score += p1 + p2 + p3 + 1
                p1, p2, p3 = 0, 0, 0
            player_num += 1
            if player_num == 9:
                player_num = 0
            
    if score > max_point:
        max_point = score
print(max_point)

