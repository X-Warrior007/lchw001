from django.conf.urls import url
from Book.views import test,variable,tags,filter,customFilter,jicheng


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
    url(r'^jicheng/$', jicheng)
]