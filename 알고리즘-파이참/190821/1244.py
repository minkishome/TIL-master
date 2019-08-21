def man(ls, num):
    for k in range(1,len(ls)+1):
        if k%num == 0:
            if ls[k-1] == 0:
                ls[k-1] = 1
            else:
                ls[k-1] = 0
    return ls

def woman(ls, num):
    left = num-1
    right = num+1
    while 1:
        if ls[left-1] == ls[right -1]:
            left -= 1
            right += 1
            if left == 0 or right == 9:
                left += 1
                right -= 1
                break
        elif ls[left - 1] != ls[right -1]:
            left += 1
            right -= 1
            break # left 값과 right 값이 정해짐
    for z in range(left-1, right):
        if ls[z] == 0:
            ls[z] = 1
        else:
            ls[z] = 0
    return ls


import sys
sys.stdin = open('1244.txt', 'r')

num_light = int(input())
light = list(map(int, input().split()))
student_num = int(input())
student_informaion = []
for i in range(student_num):
    student_informaion.append((list(map(int, input().split()))))



for z in range(student_num):
    if student_informaion[z][0] == 1: #남자일 경우
        man(light, student_informaion[z][1])
    else:
        woman(light, student_informaion[z][1])
print(",".join(map(str, light)))