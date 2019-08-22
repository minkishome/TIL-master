paper_num = int(input())
ls = [0]*paper_num
for i in range(paper_num):
    ls[i] = list(map(int, input().split())) # 색종이의 특성을 받았다.


plain = [[0]*101 for _ in range(101)] # 최대범위 지정
plain2 = [[0]*101] * 101
for k in range(paper_num): # 숫자만큼 돌려줘야함 숫자가 바뀔 좌표 x = ls[i][2] - ls[i][0], y = ls[i][3] - ls[i][1]
    # paper_x = ls[num][2] - ls[num][0] -1
    # paper_y = ls[num][2] - ls[num][0] -1
    for x in range(ls[k][0], ls[k][2]+ls[k][0]):
        for y in range(ls[k][1], ls[k][3]+ls[k][1]):
            plain[x][y] = k + 1 # 각각의 위치를 그 숫자에 맞게 변경해준다.




for u in range(paper_num):
    check = 0
    for j in plain:
        check += j.count(u+1)
    print(check)