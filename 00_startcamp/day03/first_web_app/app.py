from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello/<str:name>')
def hello(name):
    return f'hi,{name}'


@app.route('/cube/<int:num>')
def cube(num):
    return str(num ** 3)


if __name__ == '__main__':
    app.run(debug=True)
