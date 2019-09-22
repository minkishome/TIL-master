def bit_print(i): #8비트로
    output = ''
    for j in range(7, -1, -1):
        output += '1' if i & (1 << j) else '0'
    print(output)

def bit_print2(i): # 4비트로
    output = ''
    for j in range(3, -1, -1):
        output += '1' if i & (1 << j) else '0'
    return output
    # print(output)

lsls = [0, 'F', 9, 7, 'A', 3]

def two_to_ten(string):
    cnt = 0
    summ = 0
    ls = []
    while 1:
        for i in string:
            cnt += 1
            # if i == '0':
            #     continue
            if i == '1':
                summ += 2**(7-cnt)
            if cnt == 7:
                ls.append(summ)
                cnt = 0
                summ = 0
        break
    if cnt != 7:
        summ = summ//2**(7-cnt)
    ls.append(summ)
    print('-',end = ' ')
    for i in range(len(ls)):
        if i == len(ls) -1:
            print(ls[i])
            break
        print(ls[i], end = ', ')
    return



def find_pwd(asdf):
    global pwpw
    a = len(asdf)
    for i in range(a-1, -1, -1):
        if asdf[i] == 1:
            chck = asdf[i-5:i+1]
            if chck in pew.keys():
                pwpw.append(pew[chck])
                asdf = asdf[0:i+1]
                if len(asdf) < 6:
                    return pwpw
                return find_pwd(asdf)

'''
else:
    c = ord('i') - ord('A') + 10
'''
lslslsls = '01D06079861D79F99F'

ls3 = '0269FAC9A0'
print(list(lslslsls))
sen = ''
for i in ls3:
    if i not in ['A', 'B', 'C', 'D', 'E','F']:
        sen += str(bit_print2(int(i)))
    else:
        abc = (ord(i) - ord('A') + 10)
        print(abc)
        sen += str(bit_print2(abc))
        # if i =='A':
        #     sen += str(bit_print2(10))
        # if i =='B':
        #     sen += str(bit_print2(11))
        # if i =='C':
        #     sen += str(bit_print2(12))
        # if i =='D':
        #     sen += str(bit_print2(13))
        # if i =='E':
        #     sen += str(bit_print2(14))
        # if i =='F':
        #     sen += str(bit_print2(15))
print(sen)

pew = { '001101' : 0, '010011' : 1, '111011' : 2, '110001' : 3, '100011' : 4, '110111' : 5, '001011' : 6, '111101' : 7,
        '011001' : 8, '101111' : 9 }
pwpw = []
ls_find = find_pwd(sen)
print(ls_find)



# a = 0x10
# x = 0x010120304
# print( "%d = " %a, end = '')
# bit_print(a)
# print()
# print('0%X = ' %x, end = '')
# for i in range(0,4):
#     bit_print((x >> i*8) & 0xff)
# print()
# for i in range(-7,8):
#     print('%3d = ' %i, end = '')
#     bit_print(i)


# string = '00000010001101'
# two_to_ten(string)
#
# string2 = '0000000111100000011000000111100110000110000111100111100111111001100111'
# two_to_ten(string2)
#
# n = 0x00111111
# print(n)
# print(n&0xff)
# if n & 0xff:
#     print('little endian')
# else:
#     print('big endian')
#
#
# a = 0x86
# key = 0xAA
#
#

# print('a ==>', end = '')
# bit_print(a)
# print('a^=key ==>', end = '')
# a ^= key
# bit_print(a)
# print('a^=key ==>', end= '')
# a ^= key
# bit_print(a)
# print(0x50)
# c = 5
# print(c, ~c)
# print(1,~1)
# c = 8
# bit_print(8)
# bit_print(~8)
