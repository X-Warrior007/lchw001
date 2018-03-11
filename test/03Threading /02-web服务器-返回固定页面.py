import socket

def request_handler(client_socket):
    """为每个客户进行服务"""
    # 接收每个客户的请求报文

    recv_data = client_socket.recv(4096)
    if not recv_data:
        print("客户端已经断开连接")
        client_socket.close()
        return
    # print(recv_data)
    # 给客户端回复HTTP响应报文：响应行 + 响应头 +空行 + 响应体
    request_str_data = recv_data.decode()
    data_list = request_str_data.split('\r\n')
    request_line = data_list[0]
    path_info = request_line.split(' ')[1]
    print('用户请求路径%s' % path_info)
    # print(data_list)
    try:
        file = open('./static' + path_info,'rb')
        file_data = file.read()
        file.clsoe()
    except Exception as e:
        response_line = "HTTP/1.1 404 Not Found\r\n"

        # 响应头
        response_header = "Server: PythonWebServer2.0\r\n"

        # 响应体
        response_body = "ERROR!!!!!"
        response_data = response_line + response_header + "\r\n" + response_body

    # 发送
        client_socket.send(response_data.encode())
    else:
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
        request_handler(client_socket)
