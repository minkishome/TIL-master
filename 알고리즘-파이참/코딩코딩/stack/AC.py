import collections

tc = int(input())

for _ in range(tc):
    ls_func = list(input())
    N = int(input())
    # ls = collections.deque(list(map(int, input().split())))
    ls = collections.deque(list(input()))
    ls2 = collections.deque([])

    for i in range(1, N+1):
        ls2.append(ls[2*i-1])
    if ls_func.count('D') > len(ls2):
        print('error')
    else:
        for i in ls_func:
                if i == 'R':
                    ls2.reverse()
                else:
                    if len(ls2) == 0:
                        print('error')
                    else:
                        ls2.popleft()
        if len(ls2) != 0:
            print('[', end = '')
            print(','.join(map(str, ls2)) , end = '')
            print(']')
