# quiz.py



1. `input()` ; 입력값을 받는 함수, `input()` 로 출력되는 값은 무조건 문자열!(str)



``` 
name = input()
print('hi, ' + name)

--> 터미널 입력창에서 내가 무엇을 입력하기를 기다리다가, 입력하믄 hi가 프린트 되면서 입력한 값이 name자리게 들어감
--> input()을 그대로 두기 위해서는, 터미널을 새로 만들어야함.

```

```
name = input('what is your name?:, ')
print('hi, ' + name)

--> 결과

$ python quiz.py
what is your name? hyunji
hi, hyunji
```



2. `$` : 프롬프트(내가 듣고 있어 명령을 입력해죠!)
3. `ctrl+c` : 해당 명령을 종료하게 함.
4. `ctrl+d` : 해당 터미널을 종료하겠다

5. 작업단위 하나하나를 프로세스라고 불림



```
words = input('입력 고고: ')

# words의 첫 글자와 마지막 글자를 출력하라
print(words[0], words[-1])

#마지막 글자를 출력하라
hello = 'Hello, world!'
>>> hello[len(hello) - 1]    # 마지막(인덱스 12) 문자 출력
'!'

-->
$ python quiz.py
입력 고고: abcdefg
a g

====> ## 마지막 글자 출력
words[-1]
words[len(hello)-1]
words[length-1]
```



6. `unknown = list(range(length))` ; length 안에 들어간 숫자를 0-그 숫자만큼 리스트화!



## 박스 안에 든게 문자? 숫자? 참거짓? 리스트? 인지



```
print(type(words))
```



1. type = class (=자료형) : 

   1) str : 문자열 [ ' 안에 있는 것 ', " 안에 있는 것 " ] (문자열이라고 하는 것도  list의 일종)

2. list(x) : x를 리스트화해서 보여주겠다.

```
words = input('입력 고고: ')
print(type(words))
print(words[0], words[-1])

# words를 list화 해서 보여주겠다.

my_list = list(words) 
print(my_list)

--> 

$ python quiz.py
입력 고고: ajkhfklajsdhfkj
<class 'str'>
a j
## words를 list화 해서 보여주겠다.의 결과값
['a', 'j', 'k', 'h', 'f', 'k', 'l', 'a', 'j', 's', 'd', 'h', 'f', 'k', 'j']
```



*** 컴퓨터 검정시험에서 대부분 만나게 될 것은 LIST

*** print는 기본적으로 출력을 한 뒤, enter을 치게 되게 있음. 

## 'STR'을 숫자화



```
#자연수 n을 받고 1부터 n까지 출력해라
n = input('자연수를 입력하세요 : ')
print(type(n))

n = int(n)

# str => list(str) / str => int(str)
print(type(n))
# 1부터 n까지 출력해라 0 - n
#방법 1

ns = list(range(1, n+1))


 for i in ns:
    print(i)

#방법2

for i in range(n):
    print(i+1, end=' ')
```



1. int( ad ) : ad변수를 정수로 바꾸어줌

```
# 짝수/ 홀수를 구분하자. 2=> 짝, 3=> 홀

number = int(input('숫자를 입력하시오: '))

if number % 2 == 0:
    print('짝수')
else:
    print('홀수')
```

```
# fizz buzz => 3배수에서  FIzz를 나오게 하고, 5배수에서 buzz가 나오게 하고, 15배수에서 fizz buzz가 나오게 하면 됨

number = int(input('자연수를 입력하세요 : '))

for i in range(1, number+1):

    if i % 15 == 0:
        print('fizzbuzz')
    elif i % 5 == 0:
        print('buzz')
    elif i % 3 == 0:
        print('fizz')
    else:
        print(i)

==> 자판기 동전 나누기 느낌
```



**int(정수)**, **float(실수)**, **None(값없음)**, **bool(True, False)** 



## str을 dic(딕셔너리)화



```
import requests
import json

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866'

response = requests.get(url).text

print(response)

data = json.loads(response) <= str을 dic로 타입 변경

print(type(data), data)
print(data['bnusNo'])
```



* 내가 지금 잘 못하는것
  * 리스트, 딕셔너리 생성 문법
  * 문법 내 어떤 요소가 들어갈 수 있는지
  * str, int 어려워함



* '나는' '밥을' '먹는다'

  ​	*  meal = random.choice()





### 딕셔너리



1. `for key, value in data.items()` - 키값과 밸류값 둘다 나올 수 있도록 도와주는 것.



```
d = {'a':'A', 'b':'B'
}
for a in d:
print(a)
==> a, b만 나옴

for key, value in d.items():

```



### 로또 번호 동행복권에서 가져오기



```
import requests
import json

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866'

response = requests.get(url).text

print(response)

data = json.loads(response)

print(type(data), data)
print(data['bnusNo'])

real_numbers = []

for key, value in data.items():
    if 'drwtNo' in key:
        real_numbers.append(value)

print(real_numbers)

```



* `* import flask import Flask` : flask에서 Flask를 꺼낸 것. flask안에는 엄청난 양의 뭔가가 들어있음.

web을 이용할 수 있도록 도와주는 것!



# 웹

```
from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/hello')
def hello():
    return 'hi'

@app.route('/get_lotto/<int:num>')

def get_lotto():
    #1회차 로또 정보

@app.route('/pick_lotto')
def pick_lotto():
    numbers = range(1, 46)
    lucky = random.sample(numbers, 6)
    return str(lucky)

if __name__ == '__main__':
    app.run(debug=True)

```



# HTML

```
<!DOCTYPE html>
<html>
    <head>
        <!-- 백날 데이터를 써도, 사용자한테 보이지 않음. -->
        <meta charset="utf-8"> --> HTML은 무조건 "" not ''
    </head>
    <body>
    <!-- 여기에 적는 내용은 사용자들한테 보임 -->
        <h1>Today I learned</h1> --> 글자 크기 제일 큰 것
        <h2>Learn Flask</h2> --> 글자 크기 두번째로 작은 것
        <ol>
            <li>pip install flask</li> --> *
            <li>touch app.py</li>
            <li>python app.py</li>
        
        </ol>
        <h2>Learn HTML</h2>
        <ul>
            <li>doctype html</li>
            <li>head, body</li>
            <li> h1, h2, ol, ul, li</li>
        </ul>
    
    </body>
</html>
```



### 우리가 쓸수 있는 데이터들을 가져오는 방법

- scraping

- api

- package

  