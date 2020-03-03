def snail(dis, day, move):
    global h, u, d, f
    dis += move
    print(dis)
    print('dis')
    if dis > h:
        return day
    dis -= d
    move -= move_change
    print(move)
    if move < 0:
        return -1
    return snail(dis, day+1, move)


h, u , d, f = map(int, input().split())
move_change = (f/100)*u
print(move_change)
days = snail(0, 1, u)
print(days)