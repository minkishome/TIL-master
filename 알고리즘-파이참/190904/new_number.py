import sys
sys.stdin = open('new_number.txt', 'r')

def find(a, b, ls): # a = 7 b = 8
    x = 0
    y = 0
    for i in range(len(ls)):
        if a <= ls[i]:
            x = i
            break
    for j in range(len(ls)):
        if b <= ls[j]:
            y = j
            break

    x1 = ls[x] - a  # 좌표 이동 거리
    y1 = ls[y] - b

    plain_x = [x - x1, x1+1]
    plain_y = [y - y1, y1+1]

    plain = [plain_x[0] + plain_y[0], plain_x[1] + plain_y[1]]

     # a,b의 좌표점을 찾아줌
    return reverse_find(plain, ls)



def reverse_find (ls1, ls):
    c = ls1[0]+ls1[1] -1
    x = ls[c] - (c - ls1[0])
    return x





ls1 = []
ls2 = [0]
for i in range(1, 300):
    ls1.append(i)
    ls2.append(sum(ls1))


for tc in range(int(input())):
    a, b = map(int, input().split())
    print('#%d %d' %(tc+1, find(a,b,ls2)))
