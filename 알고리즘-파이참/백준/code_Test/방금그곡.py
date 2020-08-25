def solution(m, musicinfos):
    answer = ''
    ls_music = [[0]for _ in range(len(musicinfos))]
    about_music = [[]for _ in range(len(musicinfos))]
    for i in range(len(musicinfos)):
        musicinfos[i] = musicinfos[i].split(",")
        start_h, start_m = musicinfos[i][0].split(":")
        if start_h[0] == '0':
            start_h = start_h[1]
        if start_m[0] == '0':
            start_m = start_m[1]
        end_h, end_m = musicinfos[i][1].split(":")
        if end_h[0] == '0':
            end_h = end_h[1]
        if end_m[0] == '0':
            end_m = end_m[1]
        runtime = ((int(start_h)-int(end_h))*60 + int(start_m)-int(end_m))*-1
        ls_music[i] = [0]*runtime
        about_music[i] = runtime, musicinfos[i][2], trimMelody(musicinfos[i][3])

    m = trimMelody(m)
    print(about_music)
    about_music.sort(key=lambda x : x[0], reverse=True)
    for sing in about_music:
        # ab = sing[2]*(sing[0]//len(sing[2]))
        # string = ''
        # for i in range(sing[0]%len(sing[2])):
        #     string += sing[2][i]
        ret = ''
        for i in range(sing[0]):
            ret += sing[2][i%len(sing[2])]
        if m in ret:
            answer = sing[1]
        break


    return answer

import re

def trimMelody(song):
    ret=""
    # info = re.compile('[A-G]#').split(song)
    info = re.split(r'([A-G]#+)', song)
    print(info)
    for i in info:
        if len(i)==2:
            ret+=i[0].lower()
        else:
            ret+=i
    return ret

# print(solution(	"CC#BCC#BCC#BCC#B", 	['03:00,03:30,FOO,CC#B', '04:00,04:08,BAR,CC#BCC#BCC#B']	))

print(trimMelody('CC#BCC#BCC#BCC#B'))