# coding=utf-8
from flask import Flask,session
from config import Config
# 扩展包flask_session,作用是制定session信息存放的位置，对session信息签名，指定过期时间
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)
#
Session(app)

# session和cookie的区别，本质都是基于键值对的字符串，cookie把值写入到浏览器中，session相当于把键写入到浏览器中
@app.route('/setsession')
def hello_world():
    # eyJuYW1lIjp7IiBiIjoiY0hsMGFHOXVNalE9In19.DYUdVA.Al9b0gJkvA99f4NB-TvKKENzJ14
    # Zo2PvKkqbmMf6WVko6k+krV8xcddwshUg9D3US6OZCQCVUgxAGjBkHvO1G1PJOLH9+I=
    session['name'] = 'python24'
    return 'set session success'


# session信息的获取
@app.route('/getsession')
def demo1():
    resp = session.get('name')
    return resp


if __name__ == '__main__':
    app.run()
