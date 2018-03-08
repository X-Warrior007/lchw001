import time


def index():
    return "-----主页----current time is %s" % time.ctime()


def center():
    return "-----中心页面----current time is %s" % time.ctime()


def register():
    return "-----注册页面----current time is %s" % time.ctime()


def application(env, set_header):
    # 1. 调用set_header指向的函数，将response_header传递过去
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html; charset=UTF-8')]
    set_header(status, response_headers)

    # 提取url
    path_info = env['PATH_INFO']  # /index.py

    if path_info == "/index.py":
        response_body = index()
    elif path_info == "/center.py":
        response_body = center() 
    elif path_info == "/register.py":
        response_body = register()
    else:
        response_body = "-----not found you page-----"

    # 2. 通过return 将body返回
    return response_body
