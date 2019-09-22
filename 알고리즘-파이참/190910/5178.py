import sys
sys.stdin = open('5178.txt', 'r')


def traversal(N):




for tc in range(int(input())):
    N, M, L = map(int, input().split())
    tree = [0] + list(map(int, input().split()))
    n = len(ls)