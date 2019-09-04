import sys
sys.stdin = open('2048.txt', 'r')

def do_2048(ls, dir):
    global N
    stack = []
    for i in range(N):
        stack = ls[i]
        for j in range(N-1):
            if stack[j] == 0:
                continue
            for k in range(i+1, N):
                if stack[k] == 0:
                    continue
                else:
                    if stack[j] == stack[k]:




for tc in range(int(input())):
    N, dir = input().split()
    N = int(N)
    puzzle = [ list(map(int, input().split())) for _ in range(N) ]

