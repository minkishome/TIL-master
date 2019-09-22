def find(x, y, z):
    global way, short
    if x == target_x and y == target_y:
        way += 1
        short = z
        return
    else:
        dx = [1,0]
        dy = [0,1]

        for i in range(2):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x <=n and new_y <= m:
                find(new_x, new_y, z+1)

n, m = map(int, input().split())

target_x, target_y = map(int,input().split())
way = 0
short = 999
if 0 <= target_x <= n and 0 <= target_y <= m:
    find(0,0,0)
    print(short)
    print(way)
else:
    print('fail')
