import socket
import select


# 创建服务器套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 设置套接字选项
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 设置为非阻塞
server_socket.setblocking(False)

# 绑定　监听
server_socket.bind(('', 8888))
server_socket.listen(128)

# 创建ｅｐｏｌｌ对象
epoll = select.epoll()

# 将服务器套接字设置到ｅｐｏｌｌ对象的监听列表 file descriptor文件描述符
epoll.register(server_socket.fileno(), select.EPOLLIN)

# 创建集合　保存所有的在线的客户端套接字相关的数据 {1:socket1}
client_socket_list = {}
client_address_list = {}

while True:
    # 向epoll对象获取监听结果列表
    epoll_list = epoll.poll()

    # 　学号－文件描述符　　事情－事件类型
    for fd, events in epoll_list:
        # 服务器套接字　　accept()
        if fd == server_socket.fileno():
            new_client_socket, new_client_address = server_socket.accept()
            print("收到了来自%s的连接请求" % str(new_client_address))

            # 设置套接字　非阻塞
            new_client_socket.setblocking(False)
            # 添加到ｅｐｏｌｌ监听列表
            epoll.register(new_client_socket.fileno(), select.EPOLLIN|select.EPOLLET)

            # epoll.register(new_client_socket.fileno(), select.EPOLLIN)
            # 将套接字信息添加到集合
            client_socket_list[new_client_socket.fileno()] = new_client_socket
            client_address_list[new_client_socket.fileno()] = new_client_address

        # 客户端套接字   recv() EPOLLOUT 可写事件
        elif events == select.EPOLLIN:
            recv_data = client_socket_list[fd].recv(6)
            if recv_data:
                print("收到了来自%s的数据:%s" % (str(client_address_list[fd]), recv_data.decode()))
            else:
                print("收到了来自%s断开连接请求" % str(client_address_list[fd]))

                # 从eｐｏｌｌ对象的监听列表中移除
                epoll.unregister(fd)

                # 从客户端集合中移除调用相关信息
                del client_socket_list[fd]
                del client_address_list[fd]
