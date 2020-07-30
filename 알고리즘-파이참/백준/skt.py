from string import ascii_lowercase

def solution(N):
    ans = ""
    if N <= 26:
        for i in range(N):
            ans += arr[i]
        return ans
    else:
        k = 1
        ans += arr[k]
        new_N = N - k
        if new_N % 2 != 0: #홀수
            ans += arr[k+1]*new_N
        else:
            ans += arr[k+1]
            ans += arr[k+2]*(new_N-1)
        return ans

N = int(input())
arr = list(ascii_lowercase)
print(arr)
print(solution(N))

arr_str = []
arr_cost = [0]*len(S)
length = len(S)
for i in range(length-1):
    if S[i] == S[i+1]:
        arr_str.append(i)
        arr_cost[i] = C[i]
for k in range(len(arr_str)-1):





