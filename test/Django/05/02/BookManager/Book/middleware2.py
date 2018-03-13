class TestMiddleware(object):
    """自定义中间件的类"""

    def __init__(self):
        print('--------------init')

    def process_request(self, request):
        print('--------------request')

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('--------------view')

    def process_template_response(self, request, response):
        print('--------------template')
        return response

    def process_response(self, request, response):
        print('--------------response222')

        # 给任何请求的响应都写入一个相同的cookie
        response.set_cookie('test_middle','yaowoya')

        return response