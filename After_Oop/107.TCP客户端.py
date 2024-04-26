"""
套接字：一套用于网络通信的API
#
# """
# import socket
#
# # 创建一个客户端！
# tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# SERVER_INFO = ("192.168.11.16", 60010)
#
# # 连接服务器！
# tcp_client.connect(SERVER_INFO)
#
# # 发送信息
# massage = "我是123。"
# massage = massage.encode("GBK")
# tcp_client.send(massage)
#
# recv = tcp_client.recv(1024).decode("GBK")
# print(recv)
#
# tcp_client.close()


import socket
import threading

SERVER_INFO = ("192.168.11.16", 60010)


def send(tcp_client=None):
    while 1:
        input_str = input("输入你要发送的信息：")
        tcp_client.send(input_str.encode("GBK"))


def receive(tcp_client=None):
    while 1:
        recv = tcp_client.recv(1024).decode("GBK")
        print(recv)


def main():
    # 创建一个客户端！
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接服务器！
    tcp_client.connect(SERVER_INFO)

    # 创建一个子线程来发送消息！
    tread_send = threading.Thread(target=send, args=(tcp_client,))
    tread_send.start()

    tread_receive = threading.Thread(target=receive, args=(tcp_client,))
    tread_receive.start()

    tread_send.join()
    tread_receive.join()


if __name__ == '__main__':
    main()
