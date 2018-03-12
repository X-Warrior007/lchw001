from django.db import models

# Create your models here.

class BookInfo(models.Model):
    name = models.CharField(max_length=20) #图书名称
    pub_date = models.DateField(null=True) #发布日期
    readcount = models.IntegerField(default=0) #阅读量
    commentcount = models.IntegerField(default=0) #评论量
    isDelete = models.BooleanField(default=False) #逻辑删除

    #元类信息 : 修改表名
    class Meta:
        db_table = 'bookinfo'
