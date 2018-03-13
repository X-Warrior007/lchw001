from django.conf.urls import url
from Book.views import staticFile


urlpatterns = [
    # http://127.0.0.1:8000/staticfile/
    url(r'^staticfile/$', staticFile)
]