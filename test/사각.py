import sys
sys.stdin = open('사각.txt', 'r')

test_num = int(input())

for tc in range(test_num):
    info = list(map(int, input().split()))
    N = info[0]
    M = info[1]
    K = info[2]
    plain = [[0]*M for _ in range(N)]
    for n in range(N):
        a = list(map(int, input().split()))
        plain[n] = a
    plain_part = [[0]*K for _ in range(K)]
    result = 0 # 결과값
    if N != K:
        ls_sum = []  # 테두리 뺀거의 합
        for i in range(N-K+1):
            for j in range(M-K+1): # 시작점을 지정
                plain_center = []
                plus = 0
                sum_part = 0
                for x in range(K):
                    for y in range(K):
                        plain_part[x][y] = plain[i+x][j+y] # K 범위의 부분 범위가 지정됨
                for kk in plain_part:
                    plus += sum(kk) # 각 파트의 전체 합을 구함

                for x_center in range(i+1,i+K-1):
                    for y_center in range(j+1,j+K-1):
                        plain_center.append(plain[x_center][y_center]) # 초기화 해줘야한다.
                sum_part = plus -sum(plain_center)

                ls_sum.append(sum_part)
        print('#%d %d' %(tc+1, max(ls_sum)))


    else:  # N하고 K가 같은 경우
        part_sum = 0
        center_sum = 0
        for garo in plain:
            part_sum += sum(garo) # 전체 합 구함
        for k in range(K):
            for l in range(K):
                if k != 0 and k!= K-1:
                    if l != 0 and l != K-1:
                        center_sum += plain[k][l]
        result = part_sum - center_sum
        print('#%d %d' %(tc+1, result))