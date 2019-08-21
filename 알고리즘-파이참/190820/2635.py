def make_num(a):
    num_max = [a]


    for i in range(a+1):
        num_list = [a]
        j = 1
        b = num_list[0] - i
        num_list.append(b)
        while num_list[j]>=0:
            c = num_list[j-1] - num_list[j]
            if c <0:
                break
            num_list.append(c)
            j += 1

        if len(num_list) > len(num_max):
            num_max = num_list
    return num_max
ab = int(input())
result = make_num(ab)
print(len(result))
for i in range(0,len(result)-1):
    print(result[i], end=' ')
print(result[-1], end = '')