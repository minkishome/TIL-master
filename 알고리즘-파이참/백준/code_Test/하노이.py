def hanoi(num, start, to, mid, answer):
    #종료조건
    if num == 1:
        return answer.append([start, to])
    #﻿1번 기둥에 있는 n개의 원반 중 n-1개를 2번 기둥으로 옮깁니다.(3번 기둥을 거쳐감)
    hanoi(num-1, start, mid, to, answer)
    answer.append([start, to])
    #﻿2번 기둥에 있는 n-1개의 원반을 다시 3번 기둥으로 옮깁니다.(1번 기둥을 거쳐감)
    hanoi(num-1, mid, to, start, answer)
def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer)
    print(answer)
    return answer

solution(4)