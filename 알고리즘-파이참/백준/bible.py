def permu(arr, depth):
    global count
    if depth == M:
        count += 1
        print('p', count, ':', arr)
    else:
        for i in range(N):
            if not visited[i]:
                ar = arr[:]
                visited[i] = 1
                ar.append(i)
                permu(ar, depth + 1)
                visited[i] = 0
def permu_repet(arr, depth):
    global count
    if depth == M:
        count += 1
        print('pr', count, ':', arr)
    else:
        for i in range(N):
            ar = arr[:]
            ar.append(i)
            permu_repet(ar, depth + 1)
def combi(arr, depth, last):
    global count
    if depth == M:
        count += 1
        print('c', count, ':', arr)
    else:
        for i in range(last, N):
            ar = arr[:]
            ar.append(i)
            combi(ar, depth + 1, i + 1)
def combi_repet(arr, depth, last):
    global count
    if depth == M:
        count += 1
        print('cr', count, ':', arr)
    else:
        for i in range(last, N):
            ar = arr[:]
            ar.append(i)
            combi_repet(ar, depth + 1, i)
N, M = map(int, input().split())
count = 0
visited = [0] * N
# combi([], 0, 0)
permu([], 0)
# combi_repet([], 0, 0)
# permu_repet([], 0)
def comb(data, n, r):
    global cnt
    if r == 0:
        if sum(temp) == 0: # 조건
            print(temp)
            cnt += 1
            return
    elif n < r:
        return
    else:
        temp[r-1] = data[n-1]
        comb(data, n-1, r-1)
        comb(data, n-1, r)
nums = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
n = len(nums)
cnt = 0
for i in range(n):
    temp = [0] * i
    comb(nums, n, i)
print("comb: ", cnt)