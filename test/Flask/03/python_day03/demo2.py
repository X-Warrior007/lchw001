# coding=utf-8
from flask import Flask
# 导入flask_sqlalchemy扩展包
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
# 指定数据库的配置信息
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@localhost/python24'
# 使用配置文件
app.config.from_object(Config)
# 创建sqlalchemy对象,两种实例化形式
db = SQLAlchemy(app)
# db.init_app(app)

# 定义模型类,Role类User类,一对多的关系映射
class Role(db.Model):
    # 表名可以不定义,默认创建的是同类名的表名,但不是复数
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32),unique=True)
    # 关系映射定义,反向引用,在数据库中查看表结果没有实体
    # 第一个参数为多方的类名backref等于的值可以实现多对一的查询
    # us可以实现一对多的查询
    us = db.relationship('User',backref='role')

    # 输出数据库查询的可读字符串
    def __repr__(self):
        return 'role:%s' % self.name

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    email = db.Column(db.String(32),unique=True)
    pswd = db.Column(db.String(32))
    # 定义外键
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    def __repr__(self):
        return 'user:%s' % self.name

if __name__ == '__main__':
    # 删除表
    db.drop_all()
    # 创建表
    db.create_all()
    # 添加角色数据
    ro1 = Role(name='admin')
    ro2 = Role(name='user')
    # session是数据库会话对象,添加多条数据,add()添加一条数据
    db.session.add_all([ro1, ro2])
    # 提交数据到数据库
    db.session.commit()
    us1 = User(name='wang', email='wang@163.com', pswd='123456', role_id=ro1.id)
    us2 = User(name='zhang', email='zhang@189.com', pswd='201512', role_id=ro2.id)
    us3 = User(name='chen', email='chen@126.com', pswd='987654', role_id=ro2.id)
    us4 = User(name='zhou', email='zhou@163.com', pswd='456789', role_id=ro1.id)
    db.session.add_all([us1, us2, us3, us4])
    db.session.commit()

    app.run()