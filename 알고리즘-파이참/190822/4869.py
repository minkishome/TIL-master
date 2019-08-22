import sys, math
sys.stdin = open('4869.txt', 'r')

test_num = int(input())
for num in range(test_num):
    box = int(input())
    box_num = box/10
    #짝수일때 홀수일때 나눠서

    a = int(box_num//2)   #2의 최대 갯수\
    result = 0 # 만들수 있는 경우의 수
    for i in range(0,a+1): # 10과 20으로 표시할때 20이 몇개인지 알기위함
        # 2의 개수는 i, 1의 개수는 box_num - 2*i 팩토리얼 = math.factorial(n)
        num_of1 = box_num - i*2
        result += math.factorial(box_num - i)/(math.factorial(num_of1)*math.factorial(i)) * 2**i # 홀수 일때 모든 경우의 수


    print('#%d %d'%(num+1, int(result)))
