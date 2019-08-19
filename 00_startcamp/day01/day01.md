 # 190708 startcamp - day 01

## 컴퓨터 프로그래밍 언어

###  컴퓨터

컴퓨터란, 계산기다. 

### 프로그래밍

명령어의 집합, 쉽게 일 시키는 것

### 언어

약속





## Python 기초 문법 3형식

1. 저장
2. 조건
3. 반복



## Python 함수

파이썬 함수에는 내장함수와 외장함수가 있다. 

* 내장 함수
  * `print()`:  출력하는 함수
  * `range()`: 범위를 생성하는 함수
  * `list()` : 리스트를 생성하는 함수

* 외장 함수
  * `random` : 랜덤관련 함수들의 묶음
  * `random. choice()` : 리스트에서 1개 무작위 선택
  *  ` random.sample(p,k)`: 모집단에서 k개의 요소를 무작위 비복원 선택



### 로또 번호 추첨 하기

```python
import random
numbers = range(1,46)1<=x<46 --- 이때, x는 정수가 아닌 실수!
lucky_numbers = random.sample(numbers, 6)
print(lucky_numbers)
```


$$
\dfrac{a}{b}
$$


