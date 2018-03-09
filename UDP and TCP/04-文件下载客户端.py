import socket
import os

# 1 创建一个本地套接字
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2 连接服务器
IP = input("服务器ＩＰ地址:")
port = int(input("服务器端口:"))

tcp_socket.connect((IP, port))

# ３　发送文件下载请求－文件名
file_name = input("请选择一个下载的文件名:")
tcp_socket.send(file_name.encode())

file = open("new_" + file_name, "wb")

# 记录已经写入文件的数据大小
had_write_len = 0

while True:
    # ４　通过该连接　接收文件数据　－－> 写入本地
    data = tcp_socket.recv(4096)
    if data:
        file.write(data)
        had_write_len += len(data)
    else:
        # ５　文件传输完成　关闭文件　和　连接
        # 对方关掉连接
        file.close()

        # 判断已经写入文件的大小
        if had_write_len > 0:
            print("文件传输完成")
        else:
            # 移除掉空文件
            print("服务器没有这个文件")
            os.remove("new_" + file_name)

        tcp_socket.close()
        break


