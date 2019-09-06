import sys
sys.stdin = open('냉장고.txt', 'r')

def permutation(arr, r): # arr = 순열을 만들 리스트 r은 순열의 길이
    # 1.

    used = [0 for _ in range(len(arr))] # arr 리스트의 길이만큼의 0값을 넣은 리스트 생성\

    def generate(chosen, used): # chosen이 내가 만들 순열 used는 내가 썼는지 안 썼는지 확인
        # 2.
        if len(chosen) == r:
            print('-=-=-=-=--=-=-=-=-=')
            print(chosen)
            return

        # 3.
        for i in range(len(arr)):
            if not used[i]: # used[i] 0이 아닌 경우
                chosen.append(arr[i])
                print(chosen)
                print(i)
                used[i] = 1
                generate(chosen, used)
                print('===')
                print(chosen)
                print(i)
                used[i] = 0
                chosen.pop()
                print(chosen)
    generate([], used)
for tc in range(int(input())):
    N = int(input())
    ls = list(map(int, input().split()))
    ls2 = [0] * (len(ls)//2)
    for i in range(len(ls)//2):
        ls2[i] = [ls[2*i], ls[2*i+1]]


    ls3 = []
    ls3 += [ls2.pop(0)]
    ls3 += [ls2.pop(0)]
    print(ls2)
    print(permutation(ls2, 5))


#
# permutation('ABCD', 2)
# permutation([1, 2, 3, 4, 5], 3)
