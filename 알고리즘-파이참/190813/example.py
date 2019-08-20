A = 0
Matrix1 = [[0]*5 for i in range(5)]
Matrix2 = [[0]*5 for i in range(5)]
for i in range(5):
    for j in range(5):
        Matrix1[i][j] = A
        Matrix2[i][j] = A
        A += 1



def absol_minus(list1, list2):
    sum = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(5):
        for j in range(5):
            for num in range(4):
                if i+dx[num] >= 0 and  i + dx[num] < 5:
                    if j+dy[num] >= 0 and j +dy[num] < 5:
                        sum += abs(list2[i][j]-list2[i+dx[num]][j+dy[num]])
            list1[i][j] = sum
            sum = 0

    return list1
print(Matrix1)
print(absol_minus(Matrix1,Matrix2))

