import sys
​
sys.stdin = open('input.txt', 'r')
​
raw_data = list(map(int, input().split()))
​
data = []
length = max(raw_data)

while raw_data:
    temp = []
    temp.append(raw_data.pop(0))
    temp.append(raw_data.pop(0))
    data.append(temp)
​
adj_matrix = [[0 for _ in range(length+1)] for _ in range(length+1)]
​
for datum in data:
    adj_matrix[datum[0]][datum[1]] = 1
    adj_matrix[datum[1]][datum[0]] = 1
​
# for line in adj_matrix:
#     print(line)
​
stacks = [1]
check_visit = [0] + [1] + [0 for _ in range(length-1)]
route = [1]
​
while stacks:
    for idx, ver in enumerate(adj_matrix[stacks[-1]]):
        if ver and not check_visit[idx]:
            stacks.append(idx)
            route.append(idx)
            check_visit[idx] = 1
            break
    else:
        stacks.pop(-1)
​
print('-'.join(list(map(str, route))))





