def count_sort(A,B,K):
    C = [0] * K
    for i in range(0,len(B)):
        C[A[i]] += 1

    for i in range(1,len(C)):
        C[i] += C[i-1]

    for i in range(len(B)-1,-1,-1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1
    return B

data = [0,4,1,3,1,2,4,1]
sort_data = [0]*8

print(count_sort(data,sort_data,5))
