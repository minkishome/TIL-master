import re

def solution(files):
    answer = []
    ls_files = []
    temp = [re.split(r'([0-9]+)', word) for word in files]
    print(temp)
    temp = sorted(temp, key=lambda x: (x[0].lower(), int(x[1])) )
    answer = [''.join(x) for x in temp]

    return answer


files = ['img12.png', 'img10.png', 'img01.gif', 'img02.png', 'img1.png', 'IMG01.GIF', 'img2.JPG']

for i in files:
    print(i)

solution(files)