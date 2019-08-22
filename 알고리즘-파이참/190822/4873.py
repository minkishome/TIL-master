import sys
sys.stdin = open('4873.txt', 'r')

test_num = int(input())

for tc in range(test_num):
    sen = list(input())


    while 1:
        for i in range(len(sen)):
            if i == len(sen)-1:
                break
            if sen[i] == sen[i+1]:
                sen.pop(i)
                sen.pop(i)
                i = 0
                break
        if i == len(sen) - 1:
            break
    print('#%d %d' %(tc+1, len(sen)))
