import sys

sys.stdin = open('4864.txt','r')

# XYPV
# EOGGXYPVSY
# STJJ
# HOFSTJPVPP
# ZYJZXZTIBSDG
# TTXGZYJZXZTIBSDGWQLW

#스트링으로 받는다
def in_or_not(test,check):
    test_list = list(test)
    check_list = list(check)
    for i in check_list:
        if i == test_list[0]:
            if check_list[check_list.index(i):check_list.index(i)+len(test_list)] == test_list:
                return 1
            else:
                return 0



ts = int(input())
for i in range(ts):
    part = ''
    str1 = str(input())
    str2 = str(input())
    print('#%d' %(i+1) ,end = ' ' )
    print(in_or_not(str1,str2))







