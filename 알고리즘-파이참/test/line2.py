def find(char):
    global checked, n
    new_char = char[:]
    if len(char) == n:
        checked += 1
        if checked == depth:
            print(''.join(char))
        else:
            return

    else:
        for i in range(n):
            if not check[i]:
                check[i] = True
                new_char.append(ls[i])
                find(new_char)
                new_char.pop(-1)
                check[i] = False




ls = sorted(list(map(str, input().split())))
n = len(ls)
depth = int(input())
checked = 0
check = [False] * (n+1)
string = []
find(string)

