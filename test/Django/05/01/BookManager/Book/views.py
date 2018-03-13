from django.shortcuts import render

# Create your views here.


def staticFile(request):
    """加载静态图片"""

    return render(request, 'Book/staticfile.html')
