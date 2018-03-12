from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from Book.models import BookInfo

# Create your views here.


def session(request):
    """session数据存储到django_session表中"""

    # 先把状态保持的铭感信息写入到django_session表中，再把生成的session_key存储到浏览器的cookie中
    request.session['login'] = 'yes'

    return HttpResponse('session数据存储到django_session表中')


def cookie(request):
    """cookie读写"""

    # 读取浏览器发送的cookie数据
    c = request.COOKIES.get('login')
    print(c)

    # 向浏览器中写入cookie
    response = HttpResponse('写入cookie')
    # 一次只能设置一条cookie数据
    response.set_cookie('login','yes')

    return response


def login(request):
    """处理登陆逻辑"""

    # 假装在处理登陆逻辑，并处理成功
    # 需求：登陆成功后，重定向到ajax视图

    return redirect('/ajax/')


def get_json_data(request):
    """响应json数据给ajax"""

    # 查询要转json的数据:在BookInfo中
    # book_list = [BookInfo,BookInfo,BookInfo,BookInfo]
    book_list = BookInfo.objects.all()

    # [{"name":"射雕英雄传"},{"name":"神雕侠侣"},{"name":"天龙八部"},{"name":"雪山飞狐"}]
    book_dict_list = []
    for book in book_list:
        book_dict_list.append({'name':book.name})

    # {"booklist":[{"name":"射雕英雄传"},{"name":"神雕侠侣"},{"name":"天龙八部"},{"name":"雪山飞狐"}]}
    json_dict = {'booklist':book_dict_list}

    return JsonResponse(json_dict)

    """
    {
        "booklist":[
            {"name":"射雕英雄传"}，
            {"name":"天龙八部"}
        ]
    }
    """


def ajax(request):
    """提供ajax界面"""

    return render(request, 'Book/ajax.html')


def post1(request):
    """演示POST属性：一键一值和一键多值"""

    # 获取POST属性对应的QueryDict类型的对象，保存了POST请求方法发送过来的表单数据
    query_dict = request.POST
    uname = query_dict.get('uname')
    password = query_dict.get('password')
    sex = query_dict.get('sex')
    like = query_dict.getlist('like')

    str = '%s - %s -%s -%s' % (uname,password,sex,like)

    return HttpResponse(str)


def post(request):
    """提供表单界面"""

    return render(request, 'Book/post.html')


def get2(request):
    """一键多值"""

    # 获取GET属性对应的queryDict类型的对象
    query_dict = request.GET
    a = query_dict.getlist('a') # query_dict.get('a') 只会获取最后一个值
    b = query_dict.get('b')
    c = query_dict.get('c') # 如果key不存在，返回None

    str = '%s - %s -%s' % (a, b, c)

    return HttpResponse(str)


def get1(request):
    """一键一值"""

    # 获取query_dict
    query_dict = request.GET
    a = query_dict.get('a')
    b = query_dict.get('b')
    c = query_dict.get('c')

    str = '%s - %s -%s' % (a,b,c)

    return HttpResponse(str)


def get(request):
    """提供测试界面的"""

    return render(request, 'Book/get.html')


def property(request):
    """测试 path, method, GET 属性"""

    # 获取请求路径
    path = request.path
    # 获取请求方法
    method = request.method
    # 获取GET属性。查询字符串，跟具体的请求方法没有关系，只会获取URL中？后面的查询字符串
    query_dict = request.GET

    # 构造上下文
    context = {
        'path':path,
        'method':method,
        'query_dict':query_dict
    }

    # 渲染模板
    return render(request, 'Book/property.html', context)


def test2(request, num2,num1):
    """关键字参数取值"""

    str = '测试 test2 - %s - %s' % (num1, num2)

    return HttpResponse(str)


def test1(request, num1, num2):
    """学习如何从请求地址中，获取有用数据：位置参数取值"""

    str = '测试 test1 - %s - %s' % (num1,num2)

    return HttpResponse(str)


def test(request):
    """测试"""

    return HttpResponse('测试 test')
