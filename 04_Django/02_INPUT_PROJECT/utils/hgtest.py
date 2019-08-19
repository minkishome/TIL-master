import hangulutils as hg 


name = '박민기'


input1 = '박민기'
input2 = '박민기'

char_1 = [hg.KorChar(char).countstrokes() for char in input1]
char_2 = [hg.KorChar(char).countstrokes() for char in input2]
char_mix = []
for i in range(3):
    char_mix.append(char_1[i])
    char_mix.append(char_2[i])

while len(char_mix) != 2:
    for i in range(len(char_mix)):
        if i == len(char_mix)-1:
            break
        char_mix[i] += char_mix[i+1]
        if char_mix[i] >= 10:
            char_mix[i] = char_mix[i] - 10
    char_mix.pop()
alpha = ''.join(char_mix)
result = f'{alpha}%'