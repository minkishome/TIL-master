def in_square(i, j):
    if 0 <= i < n and 0 <= j < n:
        return True
    else:
        return False


def find_start(data):
    max_points = []
    max_height = max(map(max, data))
    for i in range(n):
        for j in range(n):
            if data[i][j] == max_height:
                max_points.append([i, j])
    return [max_height, max_points]


def find_path(point, point_height, depth=1, contruction=1):
    global max_length
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    for dir in range(4):
        y, x = point[0] + directions[dir][0], point[1] + directions[dir][1]
        if in_square(y, x) and not visited[y][x]:
            if data[y][x] < point_height:
                visited[y][x] = 1
                find_path([y, x], data[y][x], depth + 1, contruction)
                visited[y][x] = 0
            elif contruction > 0 and data[y][x] - point_height < k:
                for kk in range(data[y][x] - point_height + 1, k + 1):
                    visited[y][x] = 1
                    find_path([y, x], data[y][x] - kk, depth + 1, contruction - 1)
                    visited[y][x] = 0
        else:
            if max_length < depth:
                max_length = depth


T = int(input())
for tc in range(T):
    n, k = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    max_values = find_start(data)
    max_height, starting_points = max_values[0], max_values[1]
    max_length = 0
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    for point in starting_points:
        stack = [point]
        visited = [[0] * n for _ in range(n)]
        visited[point[0]][point[1]] = 1
        find_path(point, max_height)
    print("#{} {}".format(tc + 1, max_length))