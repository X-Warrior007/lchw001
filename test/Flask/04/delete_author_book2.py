# coding=utf-8
from flask import Blueprint


api = Blueprint('api',__name__)
# 再次拆分出去的文件,需要把文件再次导入到创建蓝图对象的地方
from blue_news3 import news



# 导入源文件中的模块
from author_book1 import Author,Book,db,redirect,url_for

@api.route('/delete_author<int:id>')
def del_author(id):
    # 根据id查询数据库
    # Author.query.get(id)
    author = Author.query.filter_by(id=id).first()
    db.session.delete(author)
    db.session.commit()
    # 直接重定向到视图
    return redirect(url_for('author_book'))

# 删除书籍
@api.route('/delete_book<int:id>')
def del_book(id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('author_book'))

