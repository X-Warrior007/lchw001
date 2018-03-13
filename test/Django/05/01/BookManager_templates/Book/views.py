from django.shortcuts import render,redirect
from Book.models import BookInfo
from django.http import HttpResponse
from PIL import Image, ImageDraw, ImageFont
from django.utils.six import BytesIO
from django.core.urlresolvers import reverse


# Create your views here.

def login3(request):
    """重定向到fan3"""

    # return redirect('/fan345/18/188/')
    # return redirect(reverse('book:fan3', args=(18,188)))
    return redirect(reverse('book:fan3', kwargs={'num1':18,'num2':188}))

def fan3(request, num1 ,num2):
    """接受fan3的跳转"""

    return HttpResponse('跳转到fan3成功 %s - %s' % (num1, num2))


def login2(request):
    """重定向到fan2"""

    # return redirect('/fan234/18/188/')
    return redirect(reverse('book:fan2', args=(18,188)))


def fan2(request, num1, num2):
    """接受fan2的跳转"""

    return HttpResponse('跳转到fan2成功 %s - %s' % (num1,num2))


def login1(request):
    """重定向到fan1"""

    # return redirect('/fan123/')
    return redirect(reverse('book:fan1'))


def fan1(request):
    """接受fan1的跳转"""

    return HttpResponse('跳转到fan1成功')


def fan(request):
    """提供跳转的界面"""

    return render(request, 'Book/fan.html')


def recvYZM(request):
    """接受验证码"""

    # 获取客户端传入的验证码
    client_yzm = request.POST.get('yzm')

    # 读取服务器自己存储的验证码
    server_yzm = request.session['verifycode']

    # 两个进行比较
    if client_yzm == server_yzm:
        result = '验证成功'
    else:
        result = '验证失败'

    return HttpResponse(result)


def inputYZM(request):
    """提供验证码页面"""

    return render(request, 'Book/inputyzm.html')


def verifyCode(request):
    """生成验证码"""

    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色、宽、高 (RGB random random 255)
    bgcolor = (random.randrange(20, 100), random.randrange(20, 100), 255)
    width = 100
    height = 25
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]

    # 构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    # font = ImageFont.truetype('FreeMono.ttf', 23)

    # 如果不在ubuntu操作系统上开发,那么久需要指定编码所在的操作系统的字体的绝对路径
    font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 23)

    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    # 内存文件操作
    buf = BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')


def transfer(request):
    """接受请求"""

    name = request.POST.get('name')
    money = request.POST.get('money')

    return HttpResponse('转账 %s - %s' % (name,money))


def csrf(request):
    """提供转账页面"""

    return render(request, 'Book/csrf.html')


def zhuanYi(request):
    """html转义"""

    # 不会转义
    # return HttpResponse('测试 zhuanyi')
    # 不会转义
    # return HttpResponse('<h1>测试 zhuanyi</h1>')
    # 不会转义
    # return render(request, 'Book/zhuanyi.html')

    context = {
        'name':'zxc',
        'test':'<h1>zxj</h1>'
    }

    return render(request, 'Book/zhuanyi.html', context)


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
