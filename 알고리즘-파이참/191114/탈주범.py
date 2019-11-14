import sys
sys.stdin = open('탈주범.txt', 'r')

def iswall(x, y):
    return 0 <= x < N and 0 <= y < M

def find(depth, i1, j1, i2, j2):
    global L, arr, dir
    if depth == L:
        return
    else: # i1, j1 이 기본값, i2, j2 가 변하는 값
        if iswall(i2, j2) and arr[i2][j2]:
            if i1 == i2:
                if j1 == j2 - 1: # b
                    if 'd' in dir[arr[i1][j1]] and 'b' in dir[arr[i2][j2]]:
                        if not visited[i2][j2]:
                            location.append((i2,j2))
                            visited[i2][j2] = 1
                            for k in dxdys:
                                kx, ky = i2 + k[0], j2 + k[1]
                                if iswall(kx, ky):
                                    find(depth+1, i2, j2, kx, ky)
                        return
                else: # d
                    if 'b' in dir[arr[i1][j1]] and 'd' in dir[arr[i2][j2]]:
                        if not visited[i2][j2]:
                            location.append((i2,j2))
                            visited[i2][j2] = 1
                            for k in dxdys:
                                kx, ky = i2 + k[0], j2 + k[1]
                                if iswall(kx, ky):
                                    find(depth+1, i2, j2, kx, ky)
                            return
            elif i1 != i2:
                if i1 == i2 -1: #c
                    if 'c' in dir[arr[i1][j1]] and 'a' in dir[arr[i2][j2]]:
                        if not visited[i2][j2]:
                            location.append((i2,j2))
                            visited[i2][j2] = 1
                            for k in dxdys:
                                kx, ky = i2 + k[0], j2 + k[1]
                                if iswall(kx, ky):
                                    find(depth+1, i2, j2, kx, ky)
                            return
                else: #a
                    if 'a' in dir[arr[i1][j1]] and 'c' in dir[arr[i2][j2]]:
                        if not visited[i2][j2]:
                            location.append((i2,j2))
                            visited[i2][j2] = 1
                            for k in dxdys:
                                kx, ky = i2 + k[0], j2 + k[1]
                                if iswall(kx, ky):
                                    find(depth+1, i2, j2, kx, ky)
                            return
            # print(location)

tc = int(input())
for tn in range(1, tc+1):
    N, M, R, C, L = map(int,input().split()) # N 세로 크기, M 가로 크기, R 맨홀 세로, C 맨홀 가로 위치, L 시간
    # 맨홀이 시작점 set으로 받아서 리스트 길이? que를 사용
    arr = [list(map(int, input().split())) for _ in range(N)]
    location = [(R, C)]
    dxdys = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    dir ={1: ['a','b','c','d'],
          2 : ['a', 'c'],
          3 : ['b', 'd'],
          4 : ['a', 'd'],
          5 : ['c', 'd'],
          6 : ['b', 'c'],
          7 : ['b', 'a']
          }
    visited = [[0]*M for _ in range(N)]
    visited[R][C] = 1

    for a in range(4):
        kx, ky = R + dxdys[a][0], C + dxdys[a][1]
        if iswall(kx,ky):
            find(0, R, C, kx, ky)

    # print(location)
    print(len(location))