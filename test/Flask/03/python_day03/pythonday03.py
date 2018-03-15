# coding=utf-8
from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

# 自定义过滤器1,在视图中定义函数
def double_filter(ls):
    return ls[::-2]

# 把自定义的过滤器添加到模板中,第一个参数为函数名,第二个参数为自定义的过滤器名称
app.add_template_filter(double_filter,'db2')

# 自定义过滤器2,如果内置过滤器和内置过滤器重名,会覆盖内置过滤器
@app.template_filter('reverse')
def double_filter(ls):
    return ls[::-3]


if __name__ == '__main__':
    app.run(debug=True)
