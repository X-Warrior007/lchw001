from gevent import monkey
monkey.patch_all()
import socket
import gevent
import sys

"""
1.0 版本 当用户访问服务器的  不管用户访问什么页面 都返回Helloworld
2.0                       将用户指定的页面返回 页面不存在就返回404
3.0     使用多线程同时为多个客户端进行服务器
4.0     使用多进程
5.0     使用面向对象实现
6.0     使用协程实现
7.0     使用命令行参数执行  使用形式 python3 webxxx.py 端口号
"""

class HTTPServer(object):
    def __init__(self,port):
        """初始化"""
        # 创建一个服务器套接字
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #                         套接字             地址重用选项       1设置0取消
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 绑定
        server_socket.bind(('', port))

        # 监听 被动套接字  设置已完成三次握手队列的长度
        server_socket.listen(128)

        self.server_socket = server_socket

    def request_handler(self, client_socket):
        """为每个客户进行服务"""
        # 接收每个客户的请求报文

        recv_data = client_socket.recv(4096)
        if not recv_data:
            print("客户端已经断开连接")
            client_socket.close()
            return
        # print(recv_data)
        # 对请求报文进行切割 ----> 获取请求行  -----> 获取请求行中的用户请求的资源路径
        request_str_data = recv_data.decode()
        data_list = request_str_data.split("\r\n")
        # 请求行就是第0个元素   "GET /1.html HTTP/1.1"
        # print(data_list)
        request_line = data_list[0]

        # /home/python/Desktop/1.txt

        # 请求行中第一个数据 就是用户的资源请求路径
        path_info = request_line.split(' ')[1]
        print("用户请求路径是%s" % path_info)

        if path_info == '/':
            path_info = '/grand.html'
        try:
            # ./static  + /index.html
            file = open("./static" + path_info, "rb")
            file_data = file.read()  # 如果文件过大 容易崩溃
            file.close()
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
            client_socket.sendall(response_data.encode())

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
            client_socket.sendall(response_data)
        finally:
            # 关闭套接字
            client_socket.close()

    def start(self):
        while True:
            # 从队列中取出一个客户套接字用以服务

            client_socket, client_addr = self.server_socket.accept()
            # 调用函数 对客户端进行服务
            # 创建一个协程 单独为每一个客户端进行服务器

            # 创建并且运行 协程
            gevent.spawn(self.request_handler, client_socket)


def main():
    # sys.argv 操作系统在运行进程的时候 将进程运行时的命令行参数放到argv中 ----存放的是 进程在运行时的命令行参数的列表
    # 列表中每个元素都是一个字符串

    # print(sys.argv)
    if len(sys.argv) != 2:
        print("参数错误 python3 webxxx.py 端口号")
        return

    port = sys.argv[1]
    if not port.isdigit():
        print("参数错误 python3 webxxx.py 端口号")
        return
    port_number = int(port)
    # 创建一个服务器实例
    http_server = HTTPServer(port_number)
    # 启动实例运行
    http_server.start()

if __name__ == '__main__':
    main()