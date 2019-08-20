
import sys

sys.stdin = open('color.txt','r')



def what_color(ls, num):
    red = []
    blue = []
    for i in range(num):
        if ls[i][-1] == 1:
            for a in range(ls[i][0], ls[i][2] + 1):
                for b in range(ls[i][1],ls[i][3]+1):
                    red.append((a,b))
        else:
            for c in range(ls[i][0], ls[i][2] + 1):
                for d in range(ls[i][1],ls[i][3]+1):
                    blue.append((c,d))
    purple = list(set(red) & set(blue))  # type: List[Tuple[int, int]]
    return len(purple)


tc = int(input())
for tc in range(tc):
    color_num = int(input())
    total_color = []
    for do in range(color_num):
        non_color = list(map(int,input().split()))
        total_color.append(non_color)
    print('#%d %d' %(tc+1, what_color(total_color,color_num)))











