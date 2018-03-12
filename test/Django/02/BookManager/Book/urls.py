from django.conf.urls import url
from Book.views import bookList
# from Book import views  # views.bookList

urlpatterns = [
    # http://127.0.0.1:8000/booklist/
    url(r'^booklist/$', bookList)
]