# 04_MTV_PROJECT





# model => urls=> views => template 순서라고 생각





![1565226881791](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1565226881791.png)

마스터 urls에서 path를 사용할 경우 슬래쉬는 **무조건**  뒤에 쓴다.

![1565227974626](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1565227974626.png)

일반 urls.py는 만들어야 하고 그 안에 무조건 urlpatters 리스트를 만들어 준다. views를 위해 

from. import views를 작성한다.

![1565228783627](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1565228783627.png)

templates 안에 앱 이름과 동일한 폴더를 하나 더 만들어야 제대로 읽어준다.

![1565231170300](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1565231170300.png)

HTML을 효과적으로 상속하는 방법 (오른쪽이 상속하는 애 왼쪽이 받는애)

상속받는 애 제일 위에 상속하는 애(base.html)의 정확한 위치를 적어줘야한다.

![1565231274951](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1565231274951.png)

이 상태에서 타이틀, 바디 내부만 바꾸면 된다.



- models.py를 사용

![1565238168118](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1565238168118.png)

- DateTimeField(auto_now_add = True) => 자동으로 현재 시간을 적용

  ![1565239355346](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1565239355346.png)

  from .model import Article 이란 문장으로 인해 views.py에서 models로 왔다갔다 가능

  ![1565246491751](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1565246491751.png)

  게시글 새로 만들기 redirect => 리턴값으로 redirect안에 있는 주소로 보내기

  

![1565246598651](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1565246598651.png)

![1565246608956](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1565246608956.png)



from django.db import models





​    name = models.CharField()

​    email = models.CharField()

​    birthday = models.DateTimeField()

​    age = models.IntegerField()