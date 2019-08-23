string = input().split()


alpha = ['+','-','/','*']
stack = []
norm = ''

while string:
    one = string.pop(0)
    if one in alpha:
        stack.append(one)
    else:
        norm += one
while stack:
    a = stack.pop(-1)
    norm += a

print(norm)