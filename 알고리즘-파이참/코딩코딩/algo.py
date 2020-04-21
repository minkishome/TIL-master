"""
가로 세로 길이는 2^N
모든 픽셀이 검은색이면 0
모든 픽셀이 흰색이면 1
아닐경우 가로, 세로 나눠서
4개 조각으로 나눠
x-왼쪽위-오른쪽위-왼쪽아래-오른쪽아래래

"""
answer, list_color = [], [] # answer = 정답을 넣을 곳, list_color는 전체 블록
# 기본적으로 사사분면 중 어디인지를 표현해주어야한다.
def example(N,M): # 각 꼭지점을 말해준다
    #0 N/2-1, N/2 ~ N/
    global answer # answer라는 문자열에 답을 적을 것
    if b - a == 2:
        aaa = list_color[b-a][d-c]
        if a == list_color[M][M+1] == list_color[M+1][M] == list_color[M+1][M+1]: # 길이가 2이면서 4칸의 색이 같을 경우
            answer += a
        else: # 다를 경우
            new_a = 'x' # x 뒤에 값을 넣어야하기에
            for i in range(2):
                for j in range(2):
                    new_a += list_color[i][j]
        return # 재귀함수 종료
    else:
        ls2 = [M, (N-M)/2, N] # 어디 위치인지를 알아야 하기에
        a = list_color[M][M]
        b = list_color[M][(N-M)/2]
        c = list_color[(N-M)/2][M]
        d = list_color[(N-M)/2][(N-M)/2]
        for i in range(M, (N-M)/2):
            for j in range(M, (N-M)/2): # 1
                if a == list_color[i][j]:
                    continue
                else:
                    example((N-M)/2, M)
        for i in range((N - M) / 2, N):
            for j in range(M, (N - M) / 2): #2
                if b== list_color[i][j]:
                    continue
                else:
                    example(N, (N-M)/2)
        for i in range(M, (N - M) / 2):
            for j in range((N - M) / 2, N): #3
                if c == list_color[i][j]:
                    continue
                else:
                    example((N-M)/2, M)
        for i in range((N - M) / 2, N):
            for j in range((N - M) / 2, N): #4
                if a == list_color[i][j]:
                    continue
                else:
                    example((N-M)/2, M)