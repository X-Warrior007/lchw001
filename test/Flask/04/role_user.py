# coding=utf-8
from flask import Flask
# 导入flask_sqlalchemy扩展包
from flask_sqlalchemy import SQLAlchemy
# 导入管理器对象和迁移扩展包
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

app = Flask(__name__)

# 指定数据库的连接
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@localhost/itcast'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

#　两种实例化数据库的形式
# 创建sqlalchemy实例对象
db = SQLAlchemy()
# 实例化sqlalchemy
db.init_app(app)

# 迁移的使用
manager = Manager(app)
Migrate(app,db)
# 把迁移命令添加到管理器对象中
manager.add_command('db',MigrateCommand)


# 定义模型类:Role/User
class Role(db.Model):
    # 可以不定义,默认会创建同类名的表名
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32),unique=True)
    # 创建的是关系映射,数据库中没有对应的实体字段,第一个参数User为多方的类名,backref代表的是反向引用
    # 等号左边给一方使用,backref给多方使用
    us = db.relationship("User",backref='role')

    def __repr__(self):
        return 'role:%s' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32))
    # email = db.Column(db.String(32),unique=True)
    pswd = db.Column(db.String(32))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    def __repr__(self):
        return 'user:%s' % self.name

if __name__ == '__main__':
    # app.run(debug=True)
    manager.run()


