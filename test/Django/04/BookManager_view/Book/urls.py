from django.conf.urls import url
from Book.views import test,test1,test2,property,get,get1,get2,post,post1,ajax,get_json_data
from Book.views import login,cookie,session


urlpatterns = [
    # http://127.0.0.1:8000/test/
    url(r'^test/$', test),

    # 正则的位置参数取值： http://127.0.0.1:8000/test1/18/188/
    url(r'^test1/(\d+)/(\d+)/$', test1),

    # 正则的关键字参数取值：http://127.0.0.1:8000/test2/18/188/
    # 如果使用关键字参数，那么正则里面的关键字名字一定要和视图函数的参数名字一致
    url(r'^test2/(?P<num1>\d+)/(?P<num2>\d+)/$', test2),

    # http://127.0.0.1:8000/property/
    url(r'^property/$', property),

    # http://127.0.0.1:8000/get/
    url(r'^get/$', get),
    # http://127.0.0.1:8000/get1/?a=10&b=20&c=python
    url(r'^get1/$', get1),
    # http://127.0.0.1:8000/get2/?a=10&b=20&a=python
    url(r'^get2/$', get2),

    # http://127.0.0.1:8000/post/
    url(r'^post/$', post),
    # http://127.0.0.1:8000/post1/
    url(r'^post1/$', post1),

    # http://127.0.0.1:8000/ajax/
    url(r'^ajax/$', ajax),
    url(r'^jsondata/$', get_json_data),

    # http://127.0.0.1:8000/login/
    url(r'^login/$', login),

    # http://127.0.0.1:8000/cookie/
    url(r'^cookie/$', cookie),

    # http://127.0.0.1:8000/session/
    url(r'^session/$', session)
]