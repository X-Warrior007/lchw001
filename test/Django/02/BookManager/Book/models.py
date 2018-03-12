from django.db import models

# Create your models here.

class BookInfoManager(models.Manager):
    """自定义管理器类"""

    def get_queryset(self):
        """读取父类原始的结果集，然后进行二次帅选"""

        # super(BookInfoManager, self).get_queryset() ： 已经拿到了父类的原始的查询集
        # filter ： 该过滤器会查询满足条件的数据
        return super(BookInfoManager, self).get_queryset().filter(isDelete=False)


    def create_model(self, name):
        """
        在自定义管理器类当中，给模型类增加初始化方法
        类似于 管理器对象，有个all()
        """

        # 初始化模型对象
        book = BookInfo()

        # 属性赋值
        book.name = name
        book.readcount = 0
        book.commentcount = 0

        # 返回模型对象
        return book


class BookInfo(models.Model):
    """书籍信息模型类"""

    name = models.CharField(max_length=20) # 设计书名字段
    pub_date = models.DateField(null=True)  # 发布日期
    readcount = models.IntegerField(default=0)  # 阅读量
    commentcount = models.IntegerField(default=0)  # 评论量
    isDelete = models.BooleanField(default=False)  # 逻辑删除

    # 元类信息 : 修改表名
    class Meta:
        db_table = 'bookinfo'

    # 自定义管理器对象:默认的objects即将失效
    books = models.Manager()

    # 使用自定义管理器类，自定义管理器对象
    # books = BookInfoManager()

class PeopleInfo(models.Model):
    """人物信息模型"""

    name = models.CharField(max_length=20)  # 人物姓名
    gender = models.BooleanField(default=True)  # 人物性别
    description = models.CharField(max_length=20)  # 人物描述
    isDelete = models.BooleanField(default=False)  # 逻辑删除
    book = models.ForeignKey(BookInfo)  # 外键约束，人物属于哪本书

    # 元类信息 : 修改表名
    class Meta:
        db_table = 'peopleinfo'
