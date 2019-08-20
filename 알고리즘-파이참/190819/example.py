sentence = 'a pattern matching algorithm'
pat = 'rithm'
M = len(sentence)
N = len(pat)

def Bruteforce(p,t):
    M = len(t)
    N = len(p)
    i = 0
    j = 0
    while j<M and i <N:
        if t[i] != p[j]:
            i = i-j
            j = -1
        i = i+1
        j = j+1
    if j == M :
        return i-M
    else:
        return 0

print(Bruteforce(pat,sentence))


