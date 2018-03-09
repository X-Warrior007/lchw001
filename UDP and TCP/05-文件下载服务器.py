import socket
def read_file_data(file_name):
    """获取指定文件的数据"""
    try:
        file = open(file_name,"rb")
    except Exception as e:
        print("文件不存在")
        # return None
    else:
        # 如果文件太大　会有隐患
        file_data = file.read()
        file.close()

        return file_data

#　创建一个服务器套接字　
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定端口
server_socket.bind(('', 9999))

# 将套接字设置成监听模式(被动)
server_socket.listen(128)

while True:
    # 取出一个客户端用以服务器
    client_socket, client_address = server_socket.accept()
    print("接收到来自%s 的文件下载请求" % str(client_address))

    # 接收文件名称 读取本地文件数据
    file_name = client_socket.recv(4096)

    file_data = read_file_data(file_name)
    # 将读取到文件数据发送给客户端
    if file_data:
        client_socket.send(file_data)

    # 关掉客户端关联的套接字
    client_socket.close()

# 关闭服务器套接字
# server_socket.close()
