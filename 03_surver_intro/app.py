# Views => 최고 중간 관리자.
from flask import Flask, render_template

app = Flask(__name__)    #사용을 위한 선언

@app.route('/dict/<string:word>') # Domain 뒤에 아무말이 없으면 / 삽입
def my_dict(word):
    d= {
        'apple' : '사과',
        'banana' : '바나나'
    }

    result = d.get(word)

    if result:
        return f'{word}은(는) {result}'
    else:
        f'{word}는 단어장 안에 없습니다.'

if __name__ == '__main__': #사용을 위한 선언
    app.run(debug=True)

