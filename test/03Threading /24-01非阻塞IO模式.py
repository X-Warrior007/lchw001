import socket
import time


tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_socket.connect(('192.168.115.120', 8080))

# 默认情况下　socket blocking套接字是阻塞的 ---->
# 调用 sock.setbloking(False)将套接字设置为非阻塞的

tcp_socket.setblocking(False)

while True:
    try:
        recv_data = tcp_socket.recv(4096)
    except Exception as e:
        print("no data")
        time.sleep(1)
    else:
        print(recv_data)
