import math

#126.628144987551// 경도   37.4715005347388 // 위도
pi = math.pi
c = 37.4715005347388 - math.asin(math.sin(5/(2*6317)))*180/pi
print(c)
d = abs(37.4715005347388 - c)
print(d)
a = 126.628144987551 +(180/pi)*2*math.asin(math.sin(5/(2*6371))/math.cos(37.4715005347388))
print(a)
x = abs(126.628144987551 - a)
print(x)