import time
import re


# 路由：根据不一样的请求，不一样的函数去服务器
# key是浏览器中可能输入的url
# value是url需要调用的函数的引用
# 通过这个字典，做到了只要添加一行 key-value就完成了 对应服务的设定
#url_func_dict = {
#    "/index.html": index,        
#    "/center.html": center,        
#    "/register.html": register,        
#    "/login.html": login,
#    "/unregister.html": unregister
#}
url_func_dict = dict()

def route(url):
    def set_func(func):
        url_func_dict[url] = func  # 向url_func_dict中添加一个key-value，key是url，value是对应的函数引用
        #def call_func(*args, **kwargs):
        #    return func(*args, **kwargs)
        #return call_func
    return set_func


@route("/index.html")
def index():
    # 1. 打开对应的模板文件
    # open在没有指明用什么模式打开的时候 ，默认是r
    with open("./templates/index.html") as f:
        html_content = f.read()

    # 2. 返回模板数据
    return html_content


@route("/center.html")
def center():
    # 1. 打开对应的模板文件
    # open在没有指明用什么模式打开的时候 ，默认是r
    with open("./templates/center.html") as f:
        html_content = f.read()

    # 2. 替换数据
    data_from_mysql = "这里是从mysql中查询出来的数据....."
    html_content = re.sub(r"\{%content%\}", data_from_mysql, html_content)

    # 3. 返回模板数据
    return html_content


@route("/register.html")
def register():
    return "-----注册页面----current time is %s" % time.ctime()


@route("/login.html")
def login():
    return "-----登陆页面----current time is %s" % time.ctime()


@route("/unregister.html")
def unregister():
    return "-----注销页面----current time is %s" % time.ctime()


def application(env, set_header):
    # 1. 调用set_header指向的函数，将response_header传递过去
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html; charset=UTF-8')]
    set_header(status, response_headers)

    # 提取url
    path_info = env['PATH_INFO']  # /index.html
    try:
        # 打印url_func_dict，验证是否已经通过装饰器将这个字典中需要的key-value都添加了
        print(url_func_dict)
        # url不一样，那么取出来的value，即函数的引用不一样
        func = url_func_dict[path_info]  # 如果path_info是/index.html那么也就意味着取 index函数的引用
        # 那么将来调用的时候，就调用了不一样的函数
        response_body = func()
    except Exception as ret:
        response_body = "-----not found you page-----"

    """
    if path_info == "/index.html":
        response_body = index()
    elif path_info == "/center.html":
        response_body = center() 
    elif path_info == "/register.html":
        response_body = register()
    elif path_info == "/login.html":
        response_body = login()
    else:
        response_body = "-----not found you page-----"
    """

    # 2. 通过return 将body返回
    return response_body

