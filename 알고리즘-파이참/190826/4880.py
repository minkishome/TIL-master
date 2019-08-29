import sys
sys.stdin = open('4880.txt', 'r')


def win(x, y):
    if (c[x-1] == 1 and c[y-1] == 3) or (c[x-1] == 1 and c[y-1] == 1):
        return x
    elif (c[x-1] == 2 and c[y-1] == 1) or (c[x-1] == 2 and c[y-1] == 2):
        return x
    elif (c[x-1] == 3 and c[y-1] == 2) or (c[x-1] == 3 and c[y-1] == 3):
        return x
    return y

def div(start, end):
    if start == end:
        return start
    x = div(start, (start+end)//2)
    y = div((start+end)//2+1, end)
    return win(x,y)


a = int(input())
for n in range(a):
    b = int(input())
    c = list(map(int,input().split()))
    start = 1
    end = b
    result = div(1, b)
    print('#{} {}'.format(n+1, result ))
