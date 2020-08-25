def solution(n, t, m, timetable):
    answer = ''
    bus = [[] for _ in range(24)]
    people = [[] for _ in range(24)]
    hour = 9
    ls = []
    for i in range(n):
        minute = i*t
        if i*t >= 60:
            hour, minute = 9 + (i*t)//60, (i*t)%60
        bus[hour].append(minute)
    for time in timetable:
        hour, minu = time.split(":")
        if minu[0] == '0':
            minu = minu[1]
        if hour[0] == '0':
            hour = hour[1]
        people[int(hour)].append(int(minu))
    for person in people:
        person.sort()
    # cnt = 0
    # for i in range(24):
    #     if people[i]:
    #         for person in people:
    #             print()
    #             cnt += 1
    #             if cnt == m:
    #                 print(i, cnt)
    #                 break
    #     if cnt == m:
    #         break
    '''
    보낸 버스 잇어야하고
    시간대별로 움직이면서 버스에 사람 태우고 
    9시 이전에 타는 사람들에 대해서는 미리 계산해서 사람들 태운다
    '''

    sending = 0
    flag = True
    for i in range(0, 9):
        if people[i]:
            for person in people[i]:
                sending += 1
                if sending == m:
                    answer = person
    if answer:
        return answer


    for i in range(9,24):
        if bus[i] and flag:
            for bu in bus:
                # 사람을 태운다 bu = 버스 출발 시간
                if people[i]:
                    for person in people[j]:
                        sending += 1
                        if sending == n:
                            answer = person



    return answer