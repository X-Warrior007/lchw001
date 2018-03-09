import socket


# 买个电话当总机－接受客户端连接请求　转发到分机 ---> 服务器套接字或者监听套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 使用固定号码 -- 使用固定端口
server_socket.bind(('', 8888))

# 安装服务系统　设置等待服务区的大小 --- 默认的主动套接字设置为被动套接字
# 参数是 等待服务区(客户数量)的大小
server_socket.listen(128)

while True:
    # 从等待服务区中 取出一个客户 用以服务 转接到分机之后 用分机进行服务
    #　　　　　　　　　　　　　　　　　　　　　　　　　　　　　分机　　　　　　　　　　　　　　　　　　　客户信息
    # accept没有参数 只有返回值 是一个元组(和客户端关联的套接字《通过该套接字可以和客户进行交流》, 客户端地址)

    client_socket, client_address = server_socket.accept()
    print("接收到来自%s 的连接请求" % str(client_address))

    while True:

        # recv接收客户端的数据
        # 在正常情况下　recv返回值就是　对方给我发送的数据　
        # 如果客户端断开了连接　那么recv将返回一个bytes类型0字节长度的数据　b''
        # 对于ＴＣＰ套接字来讲　只要对方关掉连接　对于本地来讲一定会收到一个bytes类型的０字节数据
        data = client_socket.recv(4096)
        if data:
            print("收到数据%s" % data.decode())
            # 给客户端回数据
            client_socket.send(data)
        else:
            print(data)
            print("客户端已经断开ＴＣＰ连接")

            # 服务完成之后 分机挂掉
            client_socket.close()
            break


# 挂掉总机
# server_socket.close()
