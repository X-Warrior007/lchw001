from django.shortcuts import render
from django.http import HttpResponse
from Book.models import BookInfo, PeopleInfo, AreaInfo
from django.db.models import F,Q,Sum

# Create your views here.


def areaList(request):
    """省市区选择"""

    # 先查询广州市
    city = AreaInfo.objects.get(name='广州市')

    # 如果，看不惯在模板中直接写查询语句，可以先在视图中完成查询，把结果集封装到上下文当中即可
    # sheng = city.parent
    # qu_list = city.areainfo_set.all()

    # 构造上下文
    context = {
        'city':city
    }

    # 渲染模板
    return render(request, 'Book/arealist.html', context)


def bookList(request):
    """测试"""

    # 查询书籍信息：使用默认的管理器对象 ： 在管理器上调用过滤器方法会返回查询集
    # book_list = BookInfo.objects.all()

    # 查询书籍信息：使用自定义的管理器对象
    # book_list = BookInfo.books.all()

    # 以下代码演示，自定义管理器的类给模型类新增初始化方法: 类比books.all()
    # book1 = BookInfo.books.create_model('zxc')
    # book2 = BookInfo.books.create_model('zxj')
    # book_list = [book1,book2]

    # 以下代码演示，限制查询集：limit 0,2
    # book_list = BookInfo.books.all()[:2]

    # 以下代码演示基础条件查询 ： filter(模型属性__条件运算符=值)
    # 1.查询id为1的书籍 : exact 判断相等,可以省虐，直接等号, pk 等价于 主键
    # book_list = BookInfo.books.filter(id=1)
    # 2.查询书名包含‘湖’的书籍 ： contains ：包含，类似于 like
    # book_list = BookInfo.books.filter(name__contains='湖')
    # 3.查询书名以‘部’结尾的书籍：endswith :以什么什么结尾；startswith以什么什么开头
    # book_list = BookInfo.books.filter(name__endswith='部')
    # 4.查询书名不为空的书籍 : isnull : 判断是否为空，False表示不为空，两个否定表示肯定 "容易懵逼"
    # book_list = BookInfo.books.filter(name__isnull=False)
    # 5.查询编号为2或4的书籍 in : 表示只能在指定的元素中选择，不表示区间 "容易懵逼"
    # book_list = BookInfo.books.filter(id__in=[2,4])
    # 6.查询编号大于2的书籍 gt 大于， gte 大于等于， lt 小于， lte 小于等于
    # book_list = BookInfo.books.filter(id__gt=2)
    # 7.查询id不等于3的书籍:exclude 查询满足条件以外的数据
    # book_list = BookInfo.books.exclude(id=3)
    # 8.查询1980年发表的书籍
    # book_list = BookInfo.books.filter(pub_date__year='1980')
    # 9.查询1990年1月1日后发表的书籍
    # book_list = BookInfo.books.filter(pub_date__gt='1990-1-1')

    # from datetime import date
    # book_list = BookInfo.books.filter(pub_date__gt=date(1990,1,1))

    # 以下代码，演示F对象和Q对象查询 ： F('模型属性')      Q(属性名__条件运算符=值) | Q(属性名__条件运算符=值)
    # 1.查询阅读量大于评论量的书籍
    # book_list = BookInfo.books.filter(readcount__gt=F('commentcount'))
    # 2.查询阅读量大于2倍评论量的书籍 : F()支持计算
    # book_list = BookInfo.books.filter(readcount__gt=F('commentcount') * 2)

    # 1.查询阅读量大于20，或编号小于3的图书
    # book_list = BookInfo.books.filter(Q(readcount__gt=20) | Q(id__lt=3))
    # 2.查询编号不等于3的书籍 ~Q()
    book_list = BookInfo.books.filter(~Q(id=3))

    # 以下代码演示聚合过滤器aggregate()；该过滤器可以调用出聚合函数的 Avg(), Sum(), max(), min(), count()
    # 需求：计算阅读量的总数 aggregate() 返回单个字典对象 {'readcount__sum': 134}
    total_count = BookInfo.books.aggregate(Sum('readcount'))

    # 以下代码演示基础关联查询
    # 1.查询编号为1的图书中所有人物信息 ： 一查多 : peopleinfo_set
    book1 = BookInfo.books.get(id=1)
    people_list1 = book1.peopleinfo_set.all()

    # 2.查询编号为1的英雄出自的书籍 ： 多查一 : people1.book : 调用关联的外键属性即可
    people1 = PeopleInfo.objects.get(id=1)
    book2 = people1.book

    # 以下代码演示内连接 ： filter(关联的模型类小写__属性名__条件运算符=值)
    # 1.查询书名为"天龙八部"的所有人物信息 ： 一查多 : 内连接需要使用外键作为关联的模型类
    people_list2 = PeopleInfo.objects.filter(book__name='天龙八部')
    # 2.查询书籍中人物的描述包含"降龙"的书籍 : 多查一
    book_list2 = BookInfo.books.filter(peopleinfo__description__contains='降龙')

    # 构造上下文
    context = {
        'book_list':book_list,
        'total_count':total_count,
        'people_list1':people_list1,
        'book2':book2,
        'people_list2':people_list2,
        'book_list2':book_list2
    }

    return render(request, 'Book/booklist.html', context)
