def backtrack(a, k, input, arr, result): # k = 깊이, input = , arr = 입력받은 리스트, result = 말그대로 result. a는 뭐????
    global MAXCANDIDATES
    global min_value
    t = 0
    c = [0] * MAXCANDIDATES
    if k == input: # write your code
        for i in range(1, k+1):
            t += arr[i-1][a[i]-1]
            if t > min_value:
                break
            elif t <= min_value and i == k: # min_value가 달라지면 그 값을 바꿔주는거
                min_value = t
                result.append(min_value)
    else:
        k+=1
        ncandidates = construct_candidates(a,k,input,c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input, arr, result)

#후보군 구하는 함수
def construct_candidates(a, k, input, c): # 여기는 지금 후보를 구하는 함수
    in_perm = [False] * NMAX

    for i in range(1,k):
        in_perm[a[i]] = True

    ncandidates = 0
    for i in range(1, input+1):
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidates += 1
    return ncandidates

#Main
MAXCANDIDATES = 100
NMAX = 100
a = [0] * NMAX

for t in range(int(input())):
    min_value = 100
    result = list()
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    backtrack(a, 3, n, arr, result) # a = idx? k, n, arr = 전체 매트릭스, result =

    print("#{} {}".format(t+1, result))

#
# def backtrack(a, ls, k, n, res): # a는 더할 값들을 만들어주는 함수, ls는 기본 함수, k는 깊이
#     global min_value
#     k = 0
#     if k == n:
#         return min_value
#     else:
#         for i in range(n): # 각 배열에서 구하는 값
#             a.append(ispromising(a, ls, k, t))
#         for t in range(1,n+1):
#             a[t] =
#         return min(res) # 최소값을 구하자
#
# def ispromising(a, ls, k, t): # 유망도 평가, 해도 되는건지?
#
#     return 1
#
# for t in range(int(input())):
#     min_value = 100
#     result = list()
#     n = int(input())
#     a = [0] * (n+1)
#     matrix = [list(map(int,input().split() for _ in range(n)))]
#     backtrack(a, matrix, n, result)
