import socket
import multiprocessing
import re


def request_handler(client_socket):
    """为每个客户进行服务"""

    recv_data = client_socket.recv(4096)
    if not recv_data:
        print("客户端已经断开连接")
        client_socket.close()
        return

    # 对接收到的数据进行解码
    request_str_data = recv_data.decode()
    # data_list = request_str_data.split("\r\n")
    # request_line = data_list[0]

    # 请求行中第一个数据 就是用户的资源请求路径
    # request_line
    # GET /index.html HTTP/1.1
    # POST /index.html HTTP/1.1
    # 通过正则表达式来提取数据，更方便
    # ret = re.match(r"[^/]+([^ ]+)", request_line)
    ret = re.match(r"[^/]+([^ ]+)", request_str_data)
    if ret:
        path_info = ret.group(1)  # /index.html
        print(">"*30, path_info)
    else:
        path_info = "/"
    print("用户请求路径是%s" % path_info)

    # 如果通过正则提取url之后，发现是/那么就意味着需要访问的是主页
    # 一般主页的名字是  /index.html
    if path_info == '/':
        path_info = '/index.html'

    try:
        # ./html/index.html
        with open("./html" + path_info, "rb") as f:
            file_data = f.read()
    except Exception as e:
        # 用户请求路径是失败了
        # 响应行
        response_line = "HTTP/1.1 404 Not Found\r\n"

        # 响应头
        response_header = "Server: PythonWebServer2.0\r\n"

        # 响应体
        response_body = "ERROR!!!!!"
        # 拼接报文
        response_data = response_line + response_header + "\r\n" + response_body
        # 发送
        client_socket.send(response_data.encode())

    else:
        # 给客户端回复HTTP响应报文：响应行 + 响应头 +空行 + 响应体

        # 响应行
        response_line = "HTTP/1.1 200 OK\r\n"

        # 响应头
        response_header = "Server: PythonWebServer1.0\r\n"

        # 响应体
        response_body = file_data

        # 拼接报文
        response_data = (response_line + response_header + "\r\n").encode() + response_body

        # 发送
        client_socket.send(response_data)
    finally:
        # 关闭套接字
        client_socket.close()

if __name__ == '__main__':
    # 创建一个服务器套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #                         套接字             地址重用选项       1设置0取消
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 绑定
    server_socket.bind(('', 9999))

    # 监听 被动套接字  设置已完成三次握手队列的长度
    server_socket.listen(128)

    while True:
        # 从队列中取出一个客户套接字用以服务

        client_socket, client_addr = server_socket.accept()
        # 调用函数 对客户端进行服务
        # 创建一个进程 单独为每一个客户端进行服务器

        # 创建执行计划
        pro = multiprocessing.Process(target=request_handler, args=(client_socket,))

        # request_handler(client_socket)
        pro.start()
        # 由于主进程和子进程是独立的数据空间 需要在主进程中关闭这个套接字对象
        # 当子进程关闭套接字的时候 这个套接字就可以真正的释放了
        client_socket.close()
