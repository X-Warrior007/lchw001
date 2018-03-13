from django.db import models

# Create your models here.
class AreaInfo(models.Model):
    name = models.CharField(max_length=30, verbose_name='地区名称') #名称
    parent = models.ForeignKey('self',null=True,blank=True, verbose_name='上级地区') #关系

    # 元类信息 ：修改表名
    class Meta:
        db_table = 'areainfo'

    def __str__(self):
        return self.name

    def title(self):
        return self.name

    # 指定方法作为列的排序依据
    title.admin_order_field = 'name'
    # 给自己定义的方法指定名称
    title.short_description = '区域'


class PictureInfo(models.Model):
    """文件上传的模型类"""

    # upload_to : 告诉上传者,文件存储到Book/
    path = models.ImageField(upload_to='Book/')

    class Meta:
        db_table = 'pictureinfo'