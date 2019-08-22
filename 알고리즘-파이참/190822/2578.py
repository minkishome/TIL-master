def compare(ls1,ls2):
    for i in range(5):
        for j in range(5):
            number = ls2[i][j]
            for x in range(5):
                for y in range(5):
                    if number == ls1[x][y]:
                        ls1[x][y] = 0  # 각각 매칭되는 지점을 0으로 바꾼다.
                        return ls1
def garo(ls1, count):
    for k in range(5):
        if sum(ls1[k]) == 0:
            count += 1
    return count

def sero(ls1, count):
    for q in range(5):
        count_sero = 0
        for l in range(5):
            if ls1[l][q] == 0:
                count_sero += 1
                # print('count_sero = %d' %(count_sero))
        if count_sero == 5:
            count += 1
    return count

def count_dia(ls1, count):
    count_dian1 = 0
    count_dian2 = 0
    for w in range(5):
        if ls1[w][w] == 0:
            count_dian1 += 1
        elif ls1[w][4-w] == 0:
            count_dian2 += 1
    if count_dian1 == 5:
        count += 1
    elif count_dian2 == 5:
        count += 1
    return count

metal_bingo = [list(map(int,input().split())) for _ in range(5)]
answer_bingo = [list(map(int,input().split())) for _ in range(5)] # 각각의 빙고를 받음
z = 0
count_call = 1



while z < 3:

    compare(metal_bingo, answer_bingo)
    if count_call >= 12:
        z = garo(metal_bingo,sero(metal_bingo,count_dia(metal_bingo,z)))
    print(z)
    count_call += 1

print(count_call)



### 함수를 이용한 방법
## 내껄아 사회자꺼 비교, 가로 세로 대각선





# 빙고가 되는지 찾기
# 가로
# for k in range(5):
#     metal_bingo[k] == [0,0,0,0,0]:
#     count += 1
# #세로
# for q in range(5):
#     count_sero = 0
#     for l in range(5):
#         if metal_bingo[l][k] == 0:
#             count_sero += 1
#     if count_sero == 5:
#         count += 1
# count_dia = 0
# #대각선
# for w in range(5):
#     if metal_bingo[k][k] == 0:
#         count_dia += 1
# if count_dia == 5:
#     count += 1


# for i in range(5):
#     for j in range(5):
#         number = answer_bingo[i][j]
#         for x in range(5):
#             for y in range(5):
#                 if number == metal_bingo[x][y]:
#                     metal_bingo[x][y] = 0   # 각각 매칭되는 지점을 0으로 바꾼다.
#                     if z >= 12: # 3줄의 빙고를 만들기 위해 필요한 최소한의 숫자 수
#                         # 가로
#                         for k in range(5):
#                             if sum(metal_bingo[k]) == 0:
#                                 count += 1
#
#                         # 세로
#                         for q in range(5):
#                             count_sero = 0
#                             for l in range(5):
#                                 if metal_bingo[l][q] == 0:
#                                     count_sero += 1
#                                     # print('count_sero = %d' %(count_sero))
#                             if count_sero == 5:
#                                 count += 1
#                                 print(count)
#                         # 대각선
#                         count_dia = 0
#                         for w in range(5):
#                             if metal_bingo[w][w] == 0:
#                                 count_dia += 1
#                         if count_dia == 5:
#                             count += 1
#                             print(count)
#                     z += 1
#         if count >= 3:
#             break
#     if count >= 3:
#         break
# print(z)
