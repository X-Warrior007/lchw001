import socket


if __name__ == '__main__':
    # 创建TCP套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 设置套接字选项
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 绑定 监听
    server_socket.bind(('',8080))

    server_socket.listen(128)

    while True:
        client_socket, client_addr = server_socket.accept()
        print("接受到来自%s的连接请求" % str(client_addr))

        recv_data = client_socket.recv(4096)
        if not recv_data:
            print("对方已经断开连接")
        else:
            print(recv_data)
        client_socket.close()