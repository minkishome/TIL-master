import copy
def move(ls, cnt):  # cnt는 사다리를 몇개 추가 시킨 것인지를
    #garo = 0
    if cnt > 3:
        return
    start_point = 0
    for i in range(N):
        garos = start_point # 시작점
        first_garos = i
        seros = 0
        while 1:
            # print(i, garos, seros, start_point, first_garos, cntt)
            if ls[seros][garos] == 0:
                seros += 1
                if seros == sero:
                    if garos == first_garos:
                        start_point += 1
                        break # 처음 순서와 같을 때 다음번째로 넘어간다.
                    else:
                        return
            else:
                if garos -1 >= 0 and ls[seros][garos-1] == 1:
                    garos = garos-1
                elif garos + 1 <= N and ls[seros][garos+1] == 1:
                    garos = garos+1
    flag = 1
    if tmp_cnt < cnt:
        res = cnt
        return
    # ## for문이 다 돌았다는 건 이제 모든 i에서 각자 간 것이므로
    # # res = cnt # 모든 경우의 수 돌고, 최소값을 뽑아줘야함
    # flag =1
    # # else:
    # #     return

def make_sadari(ls, cnt ):
    if flag:
        return
    # if cnt > 3:
    #     return -1
    else:
        lsls = ls.copy()
        for i in range(sero):
            for j in range(N-1): # 어차피 끝까지 갈 필요가 없으니깐
                if not lsls[i][j]:
                    lsls[i][j], lsls[i][j+1] = 1, 1
                    move(lsls, cnt+1)
                    # 점 세개만 선택해서 그거 구하는 방법 해야함. 조합으로 하거나 DFS? 뭐 그런거 쓰거나
                    lsls[i][j], lsls[i][j + 1] = 0, 0

        if not flag: # flag 변화 없을때..
            return -1
        else:
            return res
    # 뭔가 끝낼 수 있는 로직이 필요.......

N, M, H = map(int, input().split()) # 세로, 가로, 위치의 개수

if M > H:
    sero = M
    sadari = [[0]*N for _ in range(M)]
else:
    sero = H
    sadari = [[0]*N for _ in range(H)]
print(sero)

res = 0
flag = 0
tmp_cnt = 9999
print(sadari)
for _ in range(M):
    x, y= map(int, input().split())
    sadari[x-1][y], sadari[x-1][y-1] = 1, 1 # 사다리를 받는다.

move(sadari, 0)
if flag:
    print(0)
else:
    result = make_sadari(sadari, 0)
    print(result)


# 제일 먼저 move 함수를 실행한 다음에 make_sadari로 갔다가 다시 move를 실행해야 한다.

 # 지금 flag랑 다 바꿔야하고 while 안 깨지는거 해결해야한다
 #