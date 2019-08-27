# def make_que(N):
#     ls = [0] * N
#     for i in range(1,N+1):
#         ls[i-1] = i
#     return ls
#
# def pop_que(ls):
#     string = ''
#     for i in range(len(ls)):
#         string += str(ls[i]) + ' '
#         ls[i] = None
#     return string
#
#
# # def emptyque(ls):
#
#
# a = make_que(3)
# print(a)
# print(pop_que(a))

# 큐에 있는 사람 수, 현재 일인당 나눠주는 사탕의 수, 현재까지 나눠준 사탕의 수
people = [['a',1,0],['b',1,0],['c',1,0],['d',1,0],['e',1,0],['f',1,0],['g',1,0]]
print(people)
a = 20
qu = []
count = 0
while a > 0:
    qu.append(people[count])
    for i in qu:
        i[1] += 1
        for j in range(i[1]):
            a = a - 1
            i[2] += 1
            print(a)
            # print(qu)
            if a == 0:
                print(qu)
                print(i, j+1)

    b = qu.pop(0)
    qu.append(b)
    # print(qu)
    count += 1
