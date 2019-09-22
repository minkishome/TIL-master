import sys
import time
sys.stdin = open('score.txt', 'r')

stime(time)
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     scores = list(map(int, input().split()))
#     results = [0]
#     for i in scores:
#         for j in range(len(results)):
#             results.append(i + results[j])
#         results = list(set(results))
#     res = len(set(results))
#     print('#%d %d' % (tc, res))


# def make_score(depth, summ):
#     if depth == N:
#         return
#
#     else:
#         for i in range(0,N):
#             if not visited[i]:
#                 visited[i] = True
#                 new_summ = summ + score_list[i]
#                 score_set.add(new_summ)
#                 make_score(depth+1, new_summ)
#                 visited[i] = False
#
#
#
#
# for tc in range(int(input())):
#     N = int(input()) # 점수갯수
#     score_list = list(map(int, input().split()))
#     score_set = set()
#     visited = [0] * (N+1)
#     make_score(0,0)
#     score_set.add(0)
#     print('#%d %d' %(tc+1, len(score_set)))