import socket
import time


# 创建一个服务器套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 绑定　监听　
server_socket.bind(('', 8888))
server_socket.listen(128)

# 设置为非阻塞 accept recv在没有结果的情况下都会抛出异常
server_socket.setblocking(False)

# 保存着连接服务器的所有客户端信息 (socket, address)
client_socket_list = []
while True:
    try:
        client_socket, client_address = server_socket.accept()
    except Exception as e:
        print("暂时没有客户端连接")
        time.sleep(0.5)
        # CPU 空转--资源浪费
        # 如果时间间隔大　用户体验不好
    else:
        print("接收到客户端%s连接请求" % str(client_address))
        # 将新连接上来的套接字设置为非阻塞模式
        client_socket.setblocking(False)

        client_socket_list.append((client_socket, client_address))
    finally:
        for cli_socket,cli_addr in client_socket_list:
            try:
                recv_data = cli_socket.recv(4096)
            except Exception as e:
                print("当前客户端%s没有数据" % str(cli_addr))
            else:
                if recv_data:
                    print("收到客户端%s的数据%s" % (str(cli_addr), recv_data.decode()))
                else:
                    print("客户端%s断开连接" % str(cli_addr))
                    client_socket_list.remove((cli_socket,cli_addr))
