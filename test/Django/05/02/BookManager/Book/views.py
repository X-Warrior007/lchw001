from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.conf import settings
from Book.models import PictureInfo,AreaInfo
from django.core.paginator import Paginator

# Create your views here.

def sheng(request):
    """获取省级数据,并转JSON字典,响应给ajax"""

    # 查询省级数据 sheng_list = [AreaInfo,AreaInfo,AreaInfo,AreaInfo,...]
    sheng_list = AreaInfo.objects.filter(parent__isnull=True)

    # 构造JSON列表
    list = []
    for sheng in sheng_list:
        list.append([sheng.id, sheng.name])

    # 构造JSON字典
    sheng_json_dict = {'shenglist':list}

    # 响应JSON : ajax收到的也是如此结构如此内容的json字典
    return JsonResponse(sheng_json_dict)

"""
{
    "shenglist":[
        [id, name],
        [id, name],
    ]
}
"""

"""
{
    "shenglist":[
        {"id":id, "name":name},
        {"id":id, "name":name},
    ]
}
"""

"""
  <select id="sheng">
      <option value="100000">北京市</option>
  </select>

  <select id="shi">
      <option value="100005">昌平区</option>
  </select>

  <select id="qu">
      <option value="0">请选择</option>
  </select>
"""


def area(request):
    """提供省市区三级联动的页面"""

    return render(request, 'Book/area.html')


def page(request, page_num):
    """分页"""

    # 查询省级信息 sheng_list = [AreaInfo,AreaInfo,AreaInfo,AreaInfo,AreaInfo,AreaInfo,... 33]
    sheng_list = AreaInfo.objects.filter(parent__isnull=True)

    # 分页的需求: 对sheng_list进行分页,每页10条
    # pagenator = [AreaInfo,AreaInfo,AreaInfo,AreaInfo,AreaInfo,AreaInfo,... 33]
    paginator =  Paginator(sheng_list, 10)

    # 为了实现,当用户输入/page/ 也是默认的请求第一页的数据
    # print(type(page_num))
    if page_num == '':
        page_num = '1'

    # 度取出某一页数据 page = [AreaInfo,AreaInfo,AreaInfo,AreaInfo,AreaInfo,AreaInfo,AreaInfo,AreaInfo,AreaInfo,AreaInfo]
    page = paginator.page(page_num)  # 1 '1'

    # 构造上下文
    context = {
        'page':page
    }

    # 渲染模板
    return render(request, 'Book/page.html', context)


def recv(request):
    """接受上传的图片,内容保存的项目,地址记录到数据库"""

    # 获取图片数据
    pic = request.FILES.get('pic') # InMemoryUploadF...
    # 获取上传的文件的名字
    pic_name = pic.name
    # 准备文件存储的路径 : '/static/media/Book/mm03.jpeg'
    path = '%s/Book/%s' % (settings.MEDIA_ROOT, pic_name)

    # 需要将受到的文件内容数据,保存到项目中
    with open(path, 'ab') as file:
        for c in pic.chunks(): # chunks() 以安全守护的形式去遍历,避免大文件造成内存溢出
            file.write(c)

    # 还需要将文件保存到项目中的路径,在数据库中记录
    pictureInfo = PictureInfo()
    # 仅仅是给模型对象的path属性赋值而已
    pictureInfo.path = 'Book/%s' % pic_name
    # 以下代码才是把path属性里面的数据,写入到数据库表中
    pictureInfo.save()

    # 响应结果
    return HttpResponse('上传成功')


def upload(request):
    """提供图片上传的表单页面"""

    return render(request, 'Book/upload.html')


def staticFile(request):
    """加载静态图片"""

    return render(request, 'Book/staticfile.html')
