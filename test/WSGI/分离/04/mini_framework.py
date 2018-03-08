import time


def index():
    return "-----主页----current time is %s" % time.ctime()

def center():
    return "-----中心页面----current time is %s" % time.ctime()

def register():
    return "-----注册页面----current time is %s" % time.ctime()

def application(path_info):
    if path_info == "/index.py":
        response_body = index()
    elif path_info == "/center.py":
        response_body = center() 
    elif path_info == "/register.py":
        response_body = register()
    else:
        response_body = "-----not found you page-----"

    # 返回对应页面的body信息
    return response_body
