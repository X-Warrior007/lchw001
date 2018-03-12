from django.shortcuts import render
from Book.models import BookInfo

# Create your views here.


def jicheng(request):
    """模板继承"""

    context = {
        'name':'zxc'
    }

    return render(request, 'Book/jicheng.html', context)


def customFilter(request):
    """自定义过滤器"""

    # 查询书籍信息
    book_list = BookInfo.objects.all()

    # 构造上下文
    context = {
        'book_list': book_list
    }

    # 渲染模板
    return render(request, 'Book/customfilter.html', context)


def filter(request):
    """过滤器"""

    # 查询书籍信息
    book_list = BookInfo.objects.all()

    # 构造上下文
    context = {
        'book_list': book_list
    }

    # 渲染模板
    return render(request, 'Book/filter.html', context)


def tags(request):
    """标签"""

    # 查询书籍信息
    book_list = BookInfo.objects.all()

    # 构造上下文
    context = {
        'book_list':book_list
    }

    # 渲染模板
    return render(request, 'Book/tags.html', context)


def variable(request):
    """分析变量解析规则"""

    # 构造上下文
    user = {'age':'18'}
    context = {
        'name':'zxc',
        'user':user
    }

    return render(request, 'Book/variable.html', context)


def test(request):
    """测试模板加载逻辑"""

    # 构造上下文
    context = {
        'name':'zxc'
    }

    # 调用模板，并渲染，然后返回
    return render(request, 'Book/test.html', context)
