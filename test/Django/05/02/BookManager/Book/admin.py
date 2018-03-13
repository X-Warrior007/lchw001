from django.contrib import admin
from Book.models import AreaInfo,PictureInfo


class AreaInfoStackedInline(admin.StackedInline):
    """以块的形式,嵌入关联的模型对象"""
    model = AreaInfo # 指定要关联的模型对象
    extra = 2        # 扩展预留的块


class AreaInfoAdmin(admin.ModelAdmin):
    """AreaInfo模型类的站点管理类"""

    # 设置每页展示的数据的条数,默认是100条
    list_per_page = 10
    # 在列表的地步增加action/动作
    actions_on_bottom = True
    # 指定展示的字段
    list_display = ['id','name','parent','title']
    # 在界面的右侧增加过滤栏
    list_filter = ['name','id']
    # 增加搜索框
    search_fields = ['name']

    # 改变字段在编辑页面的顺序
    # fields = ['parent', 'name']
    # 分组:fieldsets和fields智能二选一
    fieldsets = [
        ('高级', {'fields': ['parent']}),
        ('基本', {'fields': ['name']}),
    ]
    # 以块的形式,嵌入关联的模型类
    inlines = [AreaInfoStackedInline]


# Register your models here.
admin.site.register(AreaInfo, AreaInfoAdmin)
admin.site.register(PictureInfo)
