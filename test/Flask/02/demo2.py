# coding=utf-8
from flask import Flask
from flask_script import Manager
# flask_script扩展命令行，作用可以在终端以命令的形式启动项目，可以自定义ip和port，在生产环境下，手动指定方便调试运行代码
app = Flask(__name__)
# app.config.from_object(Config)

# 实例化管理器对象，
manager = Manager(app)


@app.route('/')
def demo1():
    return '<em>demo1 run</em>'


if __name__ == '__main__':
    # app.run可以指定host和port
    # app.run()
    manager.run()


