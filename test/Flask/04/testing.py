# coding=utf-8
import unittest
from sendmail import *


# 单元测试,定义测试类,需要继承自unittest.TestCase
# class TestMail(unittest.TestCase):
#
#     # 方法名固定,会被首先执行
#     def setUp(self):
#         # 构造程序实例
#         self.app = app
#         # 构造客户端
#         self.client = self.app.test_client()
#
#     def tearDown(self):
#         pass
#
#     # 测试方法,方法名必须以test开头
#     def test_sent_mail(self):
#         resp = self.client.get('/')
#         print resp.data
#         # 断言发送结果
#         self.assertEqual(resp.data,'Sent　Succeed')

from author_book1 import *

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.app = app
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@localhost/test'
        db.create_all()
        # app.config['TESTING'] = True

    def tearDown(self):
        # 测试结束后需要移除数据库会话对象
        db.session.remove()
        """
        au = Author.query.filter_by(name='itcast').first()
        db.session.delete(au)
        """
        # db.drop_all()


    def test_data(self):
        au = Author(name='itcast')
        bk = Book(info='python')
        db.session.add_all([au,bk])
        db.session.commit()
        author = Author.query.filter_by(name='itcast').first()
        book = Book.query.filter_by(info='python').first()
        self.assertIsNotNone(author)
        self.assertIsNotNone(book)





