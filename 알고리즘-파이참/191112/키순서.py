import sys
sys.stdin = open('키순서.txt', 'r')

from collections import deque

def talltall(ls1): # ls1 : 키순서 ls2 : 전체 학생수
    global student, res
    for k in student:
        que1 = deque()
        que2 = deque()
        compare = set()
        for q in tall:
            if k == q[0]:
                compare.add(k)
                compare.add(q[1])
                que1.append(q[1])
                while que1:
                    alpha = que1.pop()
                    for z in tall:
                        if alpha == z[0]:
                            compare.add(alpha)
                            compare.add(z[1])
                            que1.append(z[1])
        ### 앞으로 뒤로

            elif k == q[1]:
                compare.add(k)
                compare.add(q[0])
                que2.append(q[0])
                while que2:
                    alpha = que2.pop()
                    for z in tall:
                        if alpha == z[1]:
                            compare.add(alpha)
                            compare.add(z[0])
                            que2.append(z[0])
        ls_compare = list(compare)
        if student == sorted(ls_compare):
            res += 1
    return


tc = int(input())
for ppp in range(1, tc+1):
    N = int(input()) # 학생들의 숫자
    M = int(input()) # 학생들 키 순서 비교
    tall = []
    tall_com = [ [0]*(N+1) for _ in range(N+1)]
    print(tall_com)
    student = []
    for z in range(1, N+1):
        student += [z]
    for _ in range(M):
        x, y = map(int, input().split())
        tall_com[x][y] = 1
        tall.append([x,y])

    print(tall)
    res = 0
    talltall(tall)
    print('#%d %d' %(ppp, res))