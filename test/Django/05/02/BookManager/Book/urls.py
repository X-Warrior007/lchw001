from django.conf.urls import url
from Book.views import staticFile,upload,recv,page,area,sheng


urlpatterns = [
    # http://127.0.0.1:8000/staticfile/
    url(r'^staticfile/$', staticFile),

    # http://127.0.0.1:8000/upload/
    url(r'^upload/$', upload),
    # http://127.0.0.1:8000/recv/
    url(r'^recv/$', recv),
    # http://127.0.0.1:8000/page/
    url(r'^page(\d*)/$', page),
    # http://127.0.0.1:8000/area/
    url(r'^area/$', area),
    # http://127.0.0.1:8000/sheng/
    url(r'^sheng/$', sheng)
]