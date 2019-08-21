import sys
sys.stdin = open('1244.txt', 'r')

num_light = int(input())
light = list(map(int, input().split()))
student_num = int(input())
student_informaion = []
for i in range(student_num):
    student_informaion.append((list(map(int, input().split()))))



for z in range(len(student_informaion)):
    if student_informaion[z][0] == 1: #남자일 경우
        num = student_informaion[z][1]
        ls = []
        for k in range(len(light)):
            if (k+1) % num == 0:
                ls.append(k)
        for j in ls:
            if light[j] == 0:
                light[j] = 1
            else:
                light[j] = 0


    if student_informaion[z][0] == 2: # 여자일 경우
        num = student_informaion[z][1]  # 각자 받은 카드의 숫자
        left1 = num -1
        right1 = num +1
        while 1:
            if light[left1-1] == light[right1-1]:
                left1 -= 1
                right1 += 1

            if len(light) < right1 or left1 == 0:
                left1 += 1
                right1 -= 1
                break
            else:
                break
        # left와 right의 숫자를 지정함

        for qq in range(left1-1, right1):
            if light[qq] == 0:
                light[qq] = 1
            else:
                light[qq] = 0
print(light)




