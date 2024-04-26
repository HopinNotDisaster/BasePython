# Socket : 套接字 (一套用于网络通信的API)

# Socket ： 方法
# socket.AF_INET
# 集合不可以序列化！！！！

# accept  服务器接受客户端链接  返回（客户端套接字，客户端地址）

"""
线程与进程：都是用于提升程序效率的技术
线程：共享的是进程的数据，多个线程之间默认就可以共享数据
    一个IO密集型(读写，网络请求)优先使用多线程
    对于Python来说，多线程并不是完全并行（全局的GIL锁）
进程：直接使用操作系统资源（ 一般都是等于CPU核心数）
    一个运算密集型(充分利用每一个CPU)优先使用多进程
池子：优化技术，预先创建一定数量的线程或者进程放入池子，使用时从池子中取
    使用完以后从新放入池子，避免反复的创建与销毁
网络编程： 多个主机上的进程相互通信
典型的通信协议：HTTP、TCP、FTP、SMTP、POP3、UDP
Socket：套接字（一套用于网络通信的API）
Socket：方法
socket.AF_INET 网络传输
socket.SOCK_STREAM 流式套接字
socket.sock
socket.socket(socket.AF_INET, socket.SOCK_STREAM) 创建TCP套接字
bind((IP, Port)) 服务器绑定IP和端口
    IP： 四部分 每一部分都位于0-255   localhost 127.0.0.1 0.0.0.0
    Port: 位于0-65535之间  一个电脑上不能重复  不要用0-1023
listen  开启监听
accept  服务器接受客户端连接  返回(客户端套接字, 客户端地址)
connect 客户端发起连接  服务器(IP, Port)
send() 发送消息 格式:bytes
recv(1024) 接受消息 返回 bytes  编码解码规则要一致
close() 双方都可以通过close关闭连接

"""

# from http.server import HTTPServer, SimpleHTTPRequestHandler
#
# SERVE_ADDRESS = ("localhost", 63333)
#
#
# def main():
#     http_serve = HTTPServer(SERVE_ADDRESS, SimpleHTTPRequestHandler)
#     http_serve.serve_forever()
#
#
# if __name__ == '__main__':
#     main()


import socket

SERVE_ADDRESS = ("192.168.11.16", 8080)

http_serve = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
http_serve.bind(SERVE_ADDRESS)
http_serve.listen()
print("http服务器启动了，正在监听......")
print("http://192.168.11.16:8080")

while 1:
    client_socket, client_info = http_serve.accept()
    print(f"{client_info}客户端正在访问")
    recv = client_socket.recv(1024).decode()
    print("客户端发来消息！")
    print(recv)

    content = "是pycharm给你显示的信息！"
    res = f"HTTP 200 OK\ncontent-Length{len(content)}\n\n{content}"
    client_socket.sendall(res.encode("GBK"))
