# coding=utf-8
from flask import Flask,render_template
from config import Config
app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def demo1():
    temp = {"user":"python24","age":16}
    list_info = [14,22,35,7,5,9]
    return render_template('index.html',temp=temp,list_info=list_info)


if __name__ == '__main__':
    # app.run可以指定host和port
    app.run()

