N = int(input()) # 드래곤 커브의 개수
# x,y = 드래곤 커브의 시작점, d는 시작 방향, g 는 세대
# 0 : x좌표가 증가 1 : y좌표가 감소 2: x 좌표가 감소 3 : y좌표가 증가

# 3 3 0 1
# 4 2 1 3
# 4 2 2 1

def dragon(x, y, d, g, cnt):
    if cnt == g:
        return
    elif cnt == 0:
        

