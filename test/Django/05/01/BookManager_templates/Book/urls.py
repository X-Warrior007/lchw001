from django.conf.urls import url
from Book.views import test,variable,tags,filter,customFilter,jicheng,zhuanYi,csrf,transfer
from Book.views import verifyCode,inputYZM,recvYZM,fan,fan1,login1,fan2,login2,fan3,login3


urlpatterns = [
    # http://127.0.0.1:8000/test/
    url(r'^test/$', test),

    # http://127.0.0.1:8000/variable/
    url(r'^variable/$', variable),

    # http://127.0.0.1:8000/tags/
    url(r'^tags/$', tags),

    # http://127.0.0.1:8000/filter/
    url(r'^filter/$', filter),

    # http://127.0.0.1:8000/customfilter/
    url(r'^customfilter/$', customFilter),

    # http://127.0.0.1:8000/jicheng/
    url(r'^jicheng/$', jicheng),

    # http://127.0.0.1:8000/zhuanyi/
    url(r'^zhuanyi/$', zhuanYi),

    # http://127.0.0.1:8000/csrf/
    url(r'^csrf/$', csrf),
    # http://127.0.0.1:8000/transfer/
    url(r'^transfer/$', transfer),

    # http://127.0.0.1:8000/verifycode/
    url(r'^verifycode/$', verifyCode),
    # http://127.0.0.1:8000/inputyzm/
    url(r'^inputyzm/$', inputYZM),
    # http://127.0.0.1:8000/recvyzm/
    url(r'^recvyzm/$', recvYZM),

    # # http://127.0.0.1:8000/fan/
    url(r'^fan/$', fan),
    # # http://127.0.0.1:8000/fan1/
    url(r'^fan123/$', fan1, name='fan1'), # name是给视图设置命名空间
    # http://127.0.0.1:8000/login1/
    url(r'^login1/$', login1),
    # http://127.0.0.1:8000/fan2/18/188/
    url(r'^fan234/(\d+)/(\d+)/$', fan2, name='fan2'),
    # http://127.0.0.1:8000/login2/
    url(r'^login2/$', login2),
    # http://127.0.0.1:8000/fan3/18/188/
    url(r'^fan345/(?P<num1>\d+)/(?P<num2>\d+)/$', fan3, name='fan3'),
    # http://127.0.0.1:8000/login3/
    url(r'^login3/$', login3)

]