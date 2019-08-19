# GIT BASH



. = 숨김 기능



touch .gitignore => git init 전에 먼저 실행

git init = 초기화 



conf / config / configure => configuration

.git이 있는 폴더  => 리포



rm -r .git/ => 전부 지우는 커맨더



code(vscode를 지칭). => code .

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

        new file:   .gitignore

커밋을 할 준비



git rm –cached – : 삭제

만약 vscode로 gitignore를 바꾸고 그 내용을 올리고 싶다면 다시 git add를 통해 파일을 올려야한다. (올라가있는 상태에서 바뀔 경우 사용)

git diff => 마지막 커밋 기준으로 어떤 차이가 있는지를 확인할 수 있다.



git log 에서 HEAD가 있는 것이 가장 처음 상태

git status에서 비어있는 폴더는 볼 수 없다.(새로 생겼음에도)

git commit는 위치가 상관없다.



vim 파일명 =>vim을 통해 프로그램 수정 (i를 눌러 입력하고 :wq를 통해 저장 후 나가기, :q!는 저장안하고 나가기)

git add . =>현재 파일을 업데이트?

git status => 현재 상태

git commit -m '메세지' 

git remote add aa(aa는 포인터, 화살표를 의미 이 뒤에 git hub 주소 넣으면된다.)

git remote -v (설정값들을 볼 수 있다.)

git remote rm XX => XX를 삭제한햣 다

$ git push -u origin master => 앞으로 -u만 붙이면 된다