from django.shortcuts import render
from django.http import HttpResponse
from Book.models import BookInfo, PeopleInfo

# Create your views here.


def peopleList(request, book_id):
    """提供人物信息列表页面"""
    # 获取book_id,从正则的组当中直接传递过来的

    # 查询用户点击的是哪本书
    book = BookInfo.objects.get(id=book_id)
    # 查询用户点击的那本书里面的 人物信息 people_list = [孙悟空，白骨精]
    people_list = book.peopleinfo_set.all()

    # 构造上下文
    context = {
        'people_list':people_list
    }

    # 调用渲染模板
    return render(request, 'Book/peoplelist.html', context)


def bookList(request):
    """提供书籍信息列表页面的"""

    # 查询所有的书籍信息 book_list = [BookInfo对象,BookInfo对象]
    book_list = BookInfo.objects.all()

    # 上下文:封装book_list
    context = {
        'book_list':book_list
    }

    return render(request, 'Book/booklist.html', context)


def test(request):
    """测试"""

    # 没有使用模板
    # return HttpResponse('测试')

    # 调用模板并渲染，然后响应给客户端 (没有传数据给模板)
    # return render(request, 'Book/test.html')

    # 上下文：是个字典，一般用于封装查询数据库之后的结果
    context = {
        'test':'我是测试数据'
    }

    # 调用模板并渲染，然后响应给客户端 (没有传数据给模板)
    return render(request, 'Book/test.html', context)