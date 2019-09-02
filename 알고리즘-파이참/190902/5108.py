import sys
sys.stdin = open('5108.txt', 'r')

from collections import deque

test_num = int(input())
for tc in range(test_num):
    N, M, L = map(int, input().split()) # N = 수열의 길이, M = 추가 횟수, L = 출력할 인덱스의 숫자
    ls = deque(map(int, input().split()))
    for _ in range(M):
        i, x = map(int, input().split())
        ls.insert(i, x)
    print('#%d %d' %(tc+1, ls[L]))

