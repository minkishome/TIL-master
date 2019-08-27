# def backtrack(a, k, input): # a = [1,2,3] k = 1 , input = 3
#     global maxcandidates
#     c = [0]* maxcandidates
#
#     if k == input:
#         for i in range(1,k+1):
#             print(a[i], end = ' ')
#         print()
#     else:
#         k+=1
#         ncandidates = construct_candidates(a, k, input, c)
#         for i in ragne(ncandidates):
#             a[k] = c[i]
#             backtrack(a,k,input)
#
# def construct_candidates(a,k,input, c):
#     in_perm = [False] * NMAX
#
#     for i in range(1,k):
#         in_perm[a[i]] = True
#
#     ncandidates = 0
#     for i in range(1,input+1):
#         if in_perm[i] == False:
#             c[ncandidates] = i
#             ncandidates += 1
#     return ncandidates

# no_0_ls = filter(lambda a: a != 0, ls2)
x = [1,2,3,2,2,2,3,4]
a = list(filter((2).__ne__, x))
print(a)


# def remove_values_from_list(the_list, val):
#     while val in the_list:
#         the_list.remove(val)
#     return the_list
# print(remove_values_from_list(x, 2))
