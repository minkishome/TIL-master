import sys
sys.stdin = open('자석.txt', 'r')


def find_index(mag_num, idx_num):
    idx = (magnet_index[mag_num] + idx_num) % 8 # 인덱스 번호 구하는 것
    return idx

def change_index(mag_num1, mag_num2, move_num): # mag_num1이 기존, mag_num2가 변화, move_num이 변화
    global flag
    if mag_num1 > mag_num2:
        a = find_index(mag_num1, 6) # 오른쪽 2번 인덱스
        b = find_index(mag_num2, 2) # 왼쪽 6번 인덱스
        if magnet[mag_num1][a] == magnet[mag_num2][b]: # 같은 극
            flag = 1
            return
        else: # 다른 극일때
            if move_num == 1:
                magnet_index[mag_num2] += 1
                if magnet_index[mag_num2] == 8:
                    magnet_index[mag_num2] = 0
            else:
                magnet_index[mag_num2] -= 1
                if magnet_index[mag_num2] == -1:
                    magnet_index[mag_num2] = 7
    else: # num1 < num2
        a = find_index(mag_num1, 2)
        b = find_index(mag_num2, 6)
        if magnet[mag_num1][a] == magnet[mag_num2][b]:
            flag = 1
            return
        else:
            if move_num == 1:
                magnet_index[mag_num2] += 1
                if magnet_index[mag_num2] == 8:
                    magnet_index[mag_num2] = 0
            else:
                magnet_index[mag_num2] -= 1
                if magnet_index[mag_num2] == -1:
                    magnet_index[mag_num2] = 7



def move_to(list_num): # 회전 시키는 정보를 닮은 리스트
    global magnet_index

    # for ls in list_num:
    a = list_num[0] - 1 # 몇번 자석을 회전 자석 range = magenet_index[num] 부터 (magenet_index[num]+8)%8
    b = list_num[1] # 1 이면 시계(인덱스 -1), -1이면 반시계(인덱스 +1)
    if b == 1:
        magnet_index[a] -= 1
        if magnet_index[a] == -1:
            magnet_index[a] = 7
    else:
        magnet_index[a] += 1
        if magnet_index[a] == 8:
            magnet_index[a] = 0
    ### 인덱스 변경, 시작하는 점

    if a == 0:
        ls = [(1,2), (2,3), (3, 4)]
        for k in ls:
            change_index(k[0] - 1, k[1] - 1, b)
            if k[0] - 1 == a:
                b *= 1
                flag = 0
            else:
                b *= -1
            if flag == 1:
                break

    if a == 1:
        ls = [(2,1), (2,3), (3,4)]
        for k in ls:
            change_index(k[0]-1, k[1]-1, b)
            if k[0] - 1 == a:
                b *= 1
                flag = 0
            else:
                b *= -1
            if flag == 1:
                break

    if a == 2:
        ls = [(3,4), (3,2), (2,1)]
        for k in ls:
            change_index(k[0]-1, k[1]-1, b)
            if k[0] - 1 == a:
                b *= 1
                flag = 0
            else:
                b *= -1
            if flag == 1:
                break

    if a == 3:
        ls = [(4,3), (3,2), (2,1)]
        for k in ls:
            change_index(k[0]-1, k[1]-1, b)
            if k[0] - 1 == a:
                b *= 1
                flag = 0
            else:
                b *= -1
            if flag == 1:
                break


tc = int(input())
for tn in range(1,tc+1):
    K = int(input()) # N = 0 S = 1
    magnet = [list(map(int, input().split())) for _ in range(4)]
    move = [list(map(int, input().split())) for _ in range(K)]
    #list_position = [2, (6,2), (6,2), 6] # 인덱스 번호 그대로 넣으면 되고 0~7 사이, %8로 접근하면 될듯
    magnet_index = [0, 0, 0, 0]# 결국 0에서 시작해서 이 위치 점을 비교할꺼니깐
    for move_info in move:
        flag = 0
        move_to(move_info)


    magnet_point = 0
    for k in range(4):
        if k == 0:
            if magnet[k][magnet_index[k]] == 1:
                magnet_point += 1
        if k == 1:
            if magnet[k][magnet_index[k]] == 1:
                magnet_point += 2
        if k == 2:
            if magnet[k][magnet_index[k]] == 1:
                magnet_point += 4
        if k == 3:
            if magnet[k][magnet_index[k]] == 1:
                magnet_point += 8
    print('#%d %d' %(tn, magnet_point))