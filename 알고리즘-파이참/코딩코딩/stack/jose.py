import collections

N, K = map(int, input().split())
ls = collections.deque([0] * N)
for i in range(N):
    ls[i] = i+1
ls_die = collections.deque([])
cnt = 0


while ls:
    a = ls.popleft()
    cnt += 1
    if cnt == K:
        ls_die.append(a)
        cnt = 0
    else:
        ls.append(a)


strin = ', '.join(map(str, ls_die))
print('<%s>' %(strin))


# for i in range(N):
#     if check[i] == 0:
#         cnt2 += 1
#         if cnt2 % K == 0:
#             ls_die.append(ls[i])
#             cnt += 1
#             cnt2 = 0
#             check[i] = 1

# while cnt != N:
#     if check[i] == 0:
#         cnt2 += 1
#         if cnt2 % K == 0:
#             ls_die.append(ls[i])
#             cnt += 1
#             cnt2 = 0
#             check[i] = 1
#     i += 1
#     if i == N:
#         i -= N