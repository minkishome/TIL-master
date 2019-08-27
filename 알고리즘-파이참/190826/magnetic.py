import sys, copy
sys.stdin = open('magnetic.txt', 'r')

def find_loca(ls): # 받은 함수의 값들의 변경, j고정에 i 변화에 따라
    count = 0
    for j in range(100): # 값이 100으로 고정되기에 일단은 100
        ls2 = [0] * 100

        for i in range(100):
            ls2[i] = ls[i][j] # 그냥 보기 좋게 변경
        no_0_ls = list(filter((0).__ne__, ls2))
        no_0_ls.insert(0, 0)
        no_0_ls.insert(-1, 0)
        # 0을 뺀 새로운 리스트를 생성
        for k in range(1,len(no_0_ls)-1): # 끝에서 하나씩 체크해 나간다. 2에 대해서만 체크
            if no_0_ls[1] == 1:
                break # 왼쪽 제일 끝이 1이면 그냥 stop
            if no_0_ls[k] == 2:
                if no_0_ls[k-1] != 1:
                    no_0_ls[k] = 0 # 옆에 1이 아닌 경우 0으로 변경
        for z in range(len(no_0_ls)-2, 0, -1):
            if no_0_ls[-2] == 2:
                break
            if no_0_ls[z] == 1:
                if no_0_ls[z+1] != 2:
                    no_0_ls[z] = 0
        # 0을 제외한 새로운 리스트에서 변화되는 모든 것을 변경함
        for l in range(1,len(no_0_ls)-1):
            if no_0_ls[l] == 1 and no_0_ls[l+1] ==2:
                count += 1
    return count





        # while ls2 != ls3:
        #     ls3 = copy.deepcopy(ls2)
        #     for k in range(100,0,-1):
        #         if ls[k] == 1: # 1에 대해서만
        #             while k != 99: # 99 이상이면 아웃임
        #                 if ls[k+1] != 2:
        #                     ls[k+1] = ls[k] # 1이 오른쪽으로 이동하면서 겹치는 경우는 결과에 영향 x
        #                 if ls[k+1] == 2:
        #                     break # 2를 만나는 경우 멈춤
        #                 k += 1
        #     for u in range(100):
        #         if ls[u] == 2: # 2에 대해서



for _ in range(10):
    tc = int(input())
    plain = [[0] for _ in range(tc)]
    for i in range(tc):
        plain[i] = list(map(int, input().split()))
    plain_change = [] # 나중에 바뀌는 리스트로 while stop에 사용
    print(find_loca(plain))



