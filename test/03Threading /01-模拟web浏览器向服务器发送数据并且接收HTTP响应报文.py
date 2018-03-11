import socket

# 创建一个套接字
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接web服务器
tcp_socket.connect(('itcastcpp.cn',80))

# 模拟浏览器发送HTTP请求报文
request_data = "GET / HTTP/1.1\r\nHost: itcastcpp.cn\r\n\r\n"
tcp_socket.send(request_data.encode())

# 接收HTTP响应报文
recv_data = tcp_socket.recv(4096)
# print(recv_data)

recv_str_data = recv_data.decode()
index = recv_str_data.find("\r\n\r\n")
print(recv_str_data[index+4:])

tcp_socket.close()
