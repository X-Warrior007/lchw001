# coding=utf-8
from flask import Flask


app = Flask(__name__)
from goods_orders import api
# 第三步:注册蓝图对象到app上
app.register_blueprint(api)

@app.route('/')
def index():
    return 'index info'

@app.route('/list')
def list():
    return 'list info'

@app.route('/detail')
def detail():
    return 'detail info'


if __name__ == '__main__':
    # 把拆分出去的文件导入到当前文件中
    from goods_orders import goods, orders
    print app.url_map
    app.run(debug=True)
