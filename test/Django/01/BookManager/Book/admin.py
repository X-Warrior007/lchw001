from django.contrib import admin
from Book.models import BookInfo, PeopleInfo

# Register your models here.


class PeopleInfoAdmin(admin.ModelAdmin):
    """定义模型类的站点管理类"""

    # 指定要展示的字段
    list_display = ['id', 'name', 'gender', 'book']


class BookInfoAdmin(admin.ModelAdmin):
    """定义模型类的站点管理类"""

    # 指定要展示的字段
    list_display = ['id', 'name']


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(PeopleInfo, PeopleInfoAdmin)
