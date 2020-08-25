import sys
sys.setrecursionlimit(3000) 

notation = '0123456789ABCEDF'

def numeral_system(number, base):
    q, r = divmod(number, base)
    n = notation[r]
    return numeral_system(q, base) + n if q else n

# result = numeral_system(2, 0)
# print(result)

def solution(n, t, m, p):
    answer = ''
    total_num = '0'
    k = t*m
    for i in range(1, k):
        total_num += numeral_system(n, i)

        if len(total_num) > k:
            break
        else:
            k += 1
    print(total_num)

    return answer

solution(2, 4, 2, 1)