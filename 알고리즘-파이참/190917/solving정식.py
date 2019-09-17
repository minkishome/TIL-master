import sys
sys.stdin = open('solving.txt', 'r')

def two_to_ten(ls):
    b = len(ls) - 1
    sum_two = 0
    for i in ls:
        sum_two += i*(2**b)
        b -= 1
    return sum_two

def three_to_ten(ls):
    b = len(ls) - 1
    sum_three = 0
    for i in ls:
        sum_three += i * (3 ** b)
        b -= 1
    return sum_three
def chan(ls_two, ls_three):
    for i in range(len(ls_two)):
        a = ls_two[i]
        if ls_two[i] == 1:
            ls_two[i] = 0
        else:
            ls_two[i] = 1 # 각 위치에 따라서 숫자를 반대되는 값으로 바꿔준다
        for j in range(len(ls_three)):
            b = ls_three[j]
            if ls_three[j] == 0:
                ls_three[j] = 1
                if two_to_ten(ls_two) == three_to_ten(ls_three):
                    return two_to_ten(ls_two)
                else:
                    ls_three[j] = 2
                    if two_to_ten(ls_two) == three_to_ten(ls_three):
                        return two_to_ten(ls_two)
            if ls_three[j] == 1:
                ls_three[j] = 0
                if two_to_ten(ls_two) == three_to_ten(ls_three):
                    return two_to_ten(ls_two)
                else:
                    ls_three[j] = 2
                    if two_to_ten(ls_two) == three_to_ten(ls_three):
                        return two_to_ten(ls_two)
            else:
                ls_three[j] = 0
                if two_to_ten(ls_two) == three_to_ten(ls_three):
                    return two_to_ten(ls_two)
                else:
                    ls_three[j] = 1
                    if two_to_ten(ls_two) == three_to_ten(ls_three):
                        return two_to_ten(ls_two)
            ls_three[j] = b
        ls_two[i] = a


for tc in range(int(input())):
    ls_two = list(map(int, input()))
    ls_three = list(map(int, input()))

    print('#%d %d' %(tc+1, chan(ls_two, ls_three)))
