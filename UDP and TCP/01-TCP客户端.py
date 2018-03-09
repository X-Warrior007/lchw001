import socket


# １　找个电话－－－创建套接字　和　服务器通信     流式报文
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2 拨号 --- 建立和服务器的沟通渠道－连接　　参数就是服务器地址
tcp_socket.connect(('192.168.115.130', 8080))

# 3 交流－说听
# TCP中使用send发送数据　只有一个参数就是需要发送的数据<bytes>
data = input("请输入你想要和服务说的话:")
tcp_socket.send(data.encode())

# 在ＴＣＰ中使用recv接收数据　参数就是　本次接收数据的最大长度
# 返回值就是　　接收到的数据<bytes>
# recv会阻塞等待　直到数据到达　
data = tcp_socket.recv(4096)
print("接收到数据:%s" % data.decode())

# ４　挂机  ---断开连接　释放套接字资源
tcp_socket.close()