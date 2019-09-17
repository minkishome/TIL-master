def comb(data, n, r):
    global cnt
    if r == 0:
        if sum(temp) == 0:
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




