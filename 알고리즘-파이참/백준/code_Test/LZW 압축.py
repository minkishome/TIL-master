from string import ascii_uppercase

def solution(msg):
    answer = []
    ls_abc = [0] + list(ascii_uppercase)
    idx = 0
    flag = len(msg)

    # print(ls_abc.index('AA'))
    while idx < flag:
        word = ''
        for i in range(idx, flag):
            word += msg[i]
            idx += 1
            if word in ls_abc:
                continue
            else: # 없을 경우
                ls_abc.append(word)
                idx -= 1
                break


        # ls_abc.append(word)
        if idx == flag:
            answer.append(ls_abc.index(word))
        else:
            answer.append(ls_abc.index(word[:-1]))
        # print(word)
        # print(ls_abc)
        # print(answer)
        # print(idx)
        # answer.append(ls_abc.index(word[:-1]))
    # print(answer)
    # print(len(msg))
    return answer

solution('KAKAO')
solution('TOBEORNOTTOBEORTOBEORNOT')