from django.conf.urls import url
from Book.views import test, bookList, peopleList


urlpatterns = [
    # http://127.0.0.1:8000/test/
    # URL,路由正则匹配，如果匹配'test/'成功，就调用该请求地址对应的test视图函数
    url(r'^test/$', test),

    # http://127.0.0.1:8000/booklist/
    url(r'^booklist/$', bookList),

    # http://127.0.0.1:8000/1/
    url(r'^(\d+)/$', peopleList)
]