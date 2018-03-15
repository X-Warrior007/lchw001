# coding=utf-8
from flask import Flask,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)




# 配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@localhost/temp1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 在请求过程中自动提交数据
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

app.config['SECRET_KEY'] = 'python24'

# 创建sqlalchemy对象
db = SQLAlchemy(app)
# db.init_app(app)

"""
案例:作者--图书
1/数据库,sqlalchemy/创建模型类作者和图书/添加数据
2/表单wtf:用来添加数据/创建表单类/实例化表单对象csrf/验证函数
3/删除功能,在模板页面中遍历数据,获取id/传给视图<int:id>/动态展示数据

"""

# 定义模型类:作者/图书
class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32),unique=True)

    def __repr__(self):
        return 'author:%s' % self.name

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    info = db.Column(db.String(32))
    leader = db.Column(db.String(32))

    def __repr__(self):
        return 'book:%s' % self.info

# 定义表单类,实现添加数据功能
class Form(FlaskForm):
    auth = StringField(validators=[DataRequired()])
    book = StringField(validators=[DataRequired()])
    submit = SubmitField(label=u'添加')

# 展示数据
@app.route('/',methods=['POST','GET'])
def author_book():
    # 实例化表单类对象
    form = Form()
    # 查询数据库
    auth = Author.query.all()
    book = Book.query.all()
    # 添加数据
    if form.validate_on_submit():
        # 获取数据
        wtf_au = form.auth.data
        wtf_bk = form.book.data
        # 存储数据
        au = Author(name=wtf_au)
        bk = Book(info=wtf_bk)
        db.session.add_all([au,bk])
        db.session.commit()
        # 添加数据后,需要动态展示数据,需要再次查询
        auth = Author.query.all()
        book = Book.query.all()
    return render_template('auth_book.html',auth=auth,book=book,form=form)

"""
try:
    author = Author.query.filter_by(id=id).first()
    db.session.delete(author)
    db.session.commit()
except:
    db.session.rollback()
    flash(******)
    abort()

"""

# # 删除作者
# @app.route('/delete_author<int:id>')
# def del_author(id):
#     # 根据id查询数据库
#     # Author.query.get(id)
#     author = Author.query.filter_by(id=id).first()
#     db.session.delete(author)
#     db.session.commit()
#     # 直接重定向到视图
#     return redirect(url_for('author_book'))
#
# # 删除书籍
# @app.route('/delete_book<int:id>')
# def del_book(id):
#     book = Book.query.get(id)
#     db.session.delete(book)
#     db.session.commit()
#     return redirect(url_for('author_book'))

# 导入蓝图对象
from delete_author_book2 import api
# 注册蓝图对象
app.register_blueprint(api)

if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    au_xi = Author(name='我吃西红柿')
    au_qian = Author(name='萧潜')
    au_san = Author(name='唐家三少')
    bk_xi = Book(info='吞噬星空', leader='罗峰')
    bk_xi2 = Book(info='寸芒', leader='李杨')
    bk_qian = Book(info='飘渺之旅', leader='李强')
    bk_san = Book(info='冰火魔厨', leader='融念冰')
    # 把数据提交给用户会话
    db.session.add_all([au_xi, au_qian, au_san, bk_xi, bk_xi2, bk_qian, bk_san])
    # 提交会话
    db.session.commit()
    print app.url_map
    app.run(debug=True)





