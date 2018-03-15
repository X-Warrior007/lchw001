# coding=utf-8

# from blue_demo import app
# 实现路由映射的解决办法,python的模块制作只能解决功能模块的调用,不能解决路由映射的问题
# 导入蓝图
from flask import Blueprint
# 第一步:创建蓝图对象
# 创建蓝图对象可以写在单个独立的脚本文件中,在其它拆分出去的文件中使用,
# 也可以在拆分出去的文件中使用
# 不可以在创建Flask程序实例的地方使用
api = Blueprint('api',__name__)


# 第二步:使用蓝图对象
@api.route('/goods')
def goods():
    return 'goods info'

@api.route('/orders')
def orders():
    return 'orders info'
