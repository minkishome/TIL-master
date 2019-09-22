

def gohome(y, z, kls, summ):
    global a
    nls = kls[:]

    if z == 4:
        a += 1
        print(summ)



    else:
        for i in range(0,n):
            if not visited[i]:
                # nls.append(case[i])
                visited[i] = True
                new_sum = summ + case[i]
                gohome(y, z+1, nls, new_sum) # 다음 순열으로 넘어가는 코드
                # nls.pop(-1)
                visited[i] = False


def all_of(z, new_sum, ls):
    global b
    if z == 5:
        b += 1
        print(new_sum)
        print(ls)


    else:
        for i in range(0,n):
            if not visited[i]:
                visited[i] = True
                ls.append(case[i])
                summ = new_sum + case[i]
                all_of(z+1, summ, ls)
                visited[i] = False
                ls.pop(-1)


def make(z, x): # 깊이를 정해주고 x는 합이나 리스트나 표현할 것
    if z == 4: # 내가 원하는 깊이, 순열의 갯수만큼을 표현
        # 내가 하려는 동작, 조건을 여기 입력


    else:
        for i in range(0,n):
            if not visited[i]:
                visited[i] = True
                # True로 만들고 나서 내가 하려는 행동을 진행 그러고 나서 재귀함수 써주고 다시 False
                

a = 0
b = 0
ls = []
case = [1,2,3,4,5,6] # n = 5
n = len(case)
visited = [False] * (n+1) # [0,0,0,0,0,0,0]
ls = []
all_of(0,0, ls)
print(b)
# gohome(0,0, ls, 0)
print(a)
