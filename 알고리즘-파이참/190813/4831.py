import sys
sys.stdin = open('4831.txt','r')

T = int(input())
for t in range(1, T+1):
    KNM = list(map(int, input().split()))
    stop = list(map(int, input().split()))
    K = KNM[0]
    N = KNM[1]


    m = []
    result = 0
    for idx in range(len(stop) - 1):
        m.append(stop[idx + 1] - stop[idx])
    m.append(N - stop[-1])
    m.append(stop[0])
    if max(m) > K:
        result = 0


    else:
        n = 0
        while n + K < N:
            if n + K in stop:
                n += K
                result += 1
            else:
                n -= 1
    print("#%d %d" % (t, result))




