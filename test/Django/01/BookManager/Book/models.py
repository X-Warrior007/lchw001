from django.db import models

# Create your models here.


class BookInfo(models.Model):
    """书籍信息模型类"""

    # 设计书名字段
    name = models.CharField(max_length=10)

    def __str__(self):
        """把模型对象以字符串的形式输出"""

        # py2需要编码utf-8,py3不需要的
        return self.name


class PeopleInfo(models.Model):
    """人物信息模型类"""

    # 设计人名字段
    name = models.CharField(max_length=10)
    # 设计性别字段
    gender = models.BooleanField()
    # 设计外键
    book = models.ForeignKey(BookInfo)

    def __str__(self):
        """把模型对象以字符串的形式输出"""
        return self.name