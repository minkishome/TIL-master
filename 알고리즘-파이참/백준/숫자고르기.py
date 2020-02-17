n = int(input())

arr = [0] * (n+1)

for i in range(1,n+1):
    arr[i] = int(input())

visited = [0] * (n+2)
max_cnt = 0
for i in range(1, n+1):
    ls1 = []
    ls2 = []
    if i != arr[i]:
        ls1.append(i), ls2.append(arr[i]) # ls1이 번호 밑에가 카드
        for k in ls2:
            if k not in ls1:
                ls1.append(k), ls2.append(arr[k])
        ls1.sort(), ls2.sort()
        if ls1 == ls2:
            cnt = len(ls1) 
            if cnt > max_cnt:
                max_cnt = cnt
                ls3 = ls1.copy()
for i in range(1, n+1):
    if i == arr[i]:
        max_cnt += 1
        ls3.append(i)
print(max_cnt)
ls3.sort()
for i in ls3:
    print(i)

