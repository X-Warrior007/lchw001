import time
import re


def index():
    # 1. 打开对应的模板文件
    # open在没有指明用什么模式打开的时候 ，默认是r
    with open("./templates/index.html") as f:
        html_content = f.read()

    # 2. 返回模板数据
    return html_content


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


def register():
    return "-----注册页面----current time is %s" % time.ctime()


def login():
    return "-----登陆页面----current time is %s" % time.ctime()


def unregister():
    return "-----注销页面----current time is %s" % time.ctime()


# 路由：根据不一样的请求，不一样的函数去服务器
# key是浏览器中可能输入的url
# value是url需要调用的函数的引用
# 通过这个字典，做到了只要添加一行 key-value就完成了 对应服务的设定
url_func_dict = {
    "/index.py": index,        
    "/center.py": center,        
    "/register.py": register,        
    "/login.py": login,
    "/unregister.py": unregister
}


def application(env, set_header):
    # 1. 调用set_header指向的函数，将response_header传递过去
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html; charset=UTF-8')]
    set_header(status, response_headers)

    # 提取url
    path_info = env['PATH_INFO']  # /index.py
    try:
        # url不一样，那么取出来的value，即函数的引用不一样
        func = url_func_dict[path_info]  # 如果path_info是/index.py那么也就意味着取 index函数的引用
        # 那么将来调用的时候，就调用了不一样的函数
        response_body = func()
    except Exception as ret:
        response_body = "-----not found you page-----"

    """
    if path_info == "/index.py":
        response_body = index()
    elif path_info == "/center.py":
        response_body = center() 
    elif path_info == "/register.py":
        response_body = register()
    elif path_info == "/login.py":
        response_body = login()
    else:
        response_body = "-----not found you page-----"
    """

    # 2. 通过return 将body返回
    return response_body

