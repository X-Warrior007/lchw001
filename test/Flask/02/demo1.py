# coding=utf-8
from config import Config
from flask import Flask,jsonify,abort,redirect,url_for

app = Flask(__name__)
app.config.from_object(Config)

"""
json
dict = "{'age':16,'name':'python24'}"

json本质是字符串，基于键值队的字符串；
作用是传输数据

xml格式：
<xml>
    <name>python24</name>
    <age>16</age>
</xml>
区别：
1/都是用来数据交互；
2/json更轻量

"""
import json


# 返回json数据
@app.route('/')
def demo1():
    my_dict = {"name":"dongGe","age":30}
    # return json.dumps(my_dict)
    # return jsonify(my_dict)
    return 'demo1 run'
# 返回状态码,通过return直接返回，可以返回不符合http协议的状态码，主要为了实现前后端的数据交互

# return jsonify(errno=666,errmsg='用户名或密码错误')
@app.route('/status')
def demo2():
    return 'demo2:',405


# 异常处理,abort,类似于python中raise语句，作用是处理异常信息，只能抛出符合http协议的状态码，abort只要捕获到异常，后面的代码不会
@app.route('/demo3')
def demo3():
    abort(404)
    return 'demo2:',403


# 自定义错误信息,errorhandler会捕获abort函数抛出的异常状态码
@app.errorhandler(404)
def demo4(e):
    return '页面找不到了，请访问某某页面'

# 重定向，当项目目录或文件发生改变的情况下，需要使用重定向，www.360buy.com
# 当活动页面不存在时，不建议直接使用redirect定向到具体的url，建议使用动态的url
# 反向解析
@app.route('/redirect')
def demo5():
    a = 'http://www.360buy.com'
    return redirect(a)

# 使用url_for,接受的参数是视图函数名，
@app.route('/demo6')
def demo6():
    return redirect(url_for('demo5'))

# 在每次请求后运行，作用可以制定前后端数据交互的响应头信息
@app.after_request
def demo7(response):
    # 修改相应头
    print 'after request run-----'
    if response.headers.get('Content-Type').startswith('text'):
        response.headers['Content-Type'] = 'application/json'
    return response


if __name__ == '__main__':
    print app.url_map
    app.run()

