N, M, H = map(int, input().split()) # 세로, 가로, 위치의 개수

def move(ls, cnt):  # cnt는 사다리를 몇개 추가 시킨 것인지를
    #garo = 0
    for i in range(N):
        garos = i # 시작점
        first_garos = i
        seros = 0
        while 1:
            if ls[seros][garos] == 0:
                seros += 1
                if seros == sero:
                    if garos == first_garos:
                        break # 처음 순서와 같을 때 다음번째로 넘어간다.
                    else:
                        return
            else:
                if garos -1 >= 0 and ls[seros][garos-1] == 1:
                    garos = garos-1
                elif garos + 1 <= N and ls[seros][garos+1] == 1:
                    garos = garos+1
    ## for문이 다 돌았다는 건 이제 모든 i에서 각자 간 것이므로
    res = cnt ## res에 cnt를 넣어준다. 그리고 조건을 하나 추가해서 밑에 makesadari를 바로 멈출 수 있도록 해야함
    return

def make_sadari(ls, cnt ):
    if cnt > 3:
        return -1
    else:
        lsls = ls
        for i in range(sero):
            for j in range(N-1): # 어차피 끝까지 갈 필요가 없으니깐
                if not lsls[i][j]:
                    lsls[i][j], lsls[i][j+1] = 1, 1
                    move(lsls, cnt+1)
                    # 점 세개만 선택해서 그거 구하는 방법 해야함. 조합으로 하거나 DFS? 뭐 그런거 쓰거나
    pass

if M > H:
    sero = M
    sadari = [[0]*N for _ in range(M)]
else:
    sero = H
    sadari = [[0]*N for _ in range(H)]
res = 0
for _ in range(M):
    x, y= map(int, input().split())
    sadari[x-1][y], sadari[x-1][y-1] = 1, 1 # 사다리를 받는다.
print(sadari)
# 제일 먼저 move 함수를 실행한 다음에 make_sadari로 갔다가 다시 move를 실행해야 한다.