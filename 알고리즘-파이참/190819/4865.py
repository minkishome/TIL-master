import sys
sys.stdin = open('4865.txt', 'r')

tc = int(input())

for num in range(tc):
    ls1 = list(input())
    ls_dict = list(input())
    com_dict = {a: ls_dict.count(a) for a in ls_dict}
    ls_num = [0]*len(ls1)
    for i in range(len(ls1)):
        ls_num[i] = com_dict[ls1[i]]
    print('#%d %d' %(num+1, max(ls_num)))