# what is git

 git : scm(source code manager) / vcs(version control system)

git => 버젼 관리를 해주는 감시카메라



1) git 용어

* touch 파일 생성
* cd : 이동

* rm : 파일 삭제

* ~ : 홈(student)

* .. : 내 위에 있는 상위 폴더



2) git  명령어

- 'git init' : 깃아~ 시작하자
- git status : 깃아 상태를 알려줘
- python -V : 파이썬아 버젼이 몇이야?
- ls = list : 해당 폴더에 파일 뭐뭐 있니
- git add 파일명 : 이제 깃이 해당 파일 암 또는 깃아 잠깐만 상태를 멈추고 봐봐{폴더도 add할 수 있음}

*  git commit -m '처음 만들었음' : 버전에 메시지를 만드는 것
* git config --global user.email 'nillcafri123@gmail.com'
*  git config --global user.name 'kim hyun ji'
* commit : 찰칵, 지금 현 상태를 사진찍어 저장하는 것과 같음

*  git log : 사진 한장마다의 시간상 역순으로 여태껏 저장한 내용이 나옴. 사진(commit)의 로그를 보여줌
* 'git add <filename>'
* 'git commit -m '<message>'
*  변경사항 저장
*  git add <filename>
* git commit -m'<message>'
* git status : 상태를 물어보는 명령어
* mkdir :  폴더 만들기 
*  : space 조심(다 새 파일명이 될 수 도)

* git add _A 또는 gis add . : 지금 내가 있는 곳을 통째로 다 사진 찍겠다. 

```
git remote add origin https://github.com/ichhjkim/practice_git.git
-> git hub에 내 파일 보내는 화살표 방향을 가르키는 것
git push -u origin master
-> 이제 그 방향으로 보내
```



* origin : 가장 메인, 
* pwd : 내가 어디에 있는지 알려주는 것



# 웹에서의 커뮤니케이션 방식 : 요청과 응답(response)



요청 ---> 주소(url) --> 응답

응답 ---> 문서(HTML, XML, Json 등) ---> 요청



클릭/엔터은 주소창(url)이 바뀌게 해주는 것.

핵심은 주소가 바뀌는 것



****확장자는 내가 구분하려고 하는 것이지, 컴퓨터보고 구분하라고 하는 것이 아님****



## import bs4



bs4. BeautifulSoup(response) --> 코드를 예뻐보이게 나오는..



`requests.get(url).text` --> 해당 url에서 text를 긁어옴

`text = bs4.BeautifulSoup(response, 'html.parser')`

`kospi = text.select_one('#KOSPI_now')`



```import requests'
#코스피 지수 네이버에서 긁어오는 코드

import requests
import bs4

url = 'https://finance.naver.com/sise/'
response = requests.get(url).text

# 요청을 통해서 ___에 있는 것을 가져오겠다. 뱉어내겠다.

# python scraping.py

text = bs4.BeautifulSoup(response, 'html.parser')

kospi = text.select_one('#KOSPI_now')

print(kospi.text)

```

``` 환율 가져오는 코드
#환율 가져오는 코드
```

```
import bs4

import requests



url = 'https://www.melon.com/chart/index.htm'



headers = {'User-Agent': ':)'}



response = requests.get(url, headers=headers).text

text = bs4.BeautifulSoup(response, 'html.parser')



rows = text.select('.lst50')



for row in rows:

​    rank = row.select_one('td:nth-child(2) > div > span.rank').text

​    title = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span').text

​    artist = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text



​    print(rank, title, artist)
```



## file control



```
#csv형식
1, 술이야, 바이브
2, 주저하는 .., 잔나비
--> ,로 구분하는 것이 핵심
```



2, 주저하는 .., 잔나비

```
lunches = {
    '양자강' : '02-557-4211',
    '김밥카페' : '02-553-3181',
    '순남시래기' : '02-508-0087'
}
 방법1
 with open('lunch.csv', 'w', encoding='utf-8') as f:
    for lunh in lunches:
        print(lunch)
        print(luncches[lunch])
방법2
with open('lunch.csv', 'w', encoding='utf-8') as f:
    for name, phone in lunches.items():
        f. write(f'{name}, {phone}\n')
```

