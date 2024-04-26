import threading
import socket

SERVE_ADDRESS = ("0.0.0.0", 60016)

client_num = []  # 里面放的是套接字！


def accept_massage(client_socket):
    while 1:
        recv_bytes = client_socket.recv(1024)
        if len(recv_bytes) > 0:
            recv_str = recv_bytes.decode(encoding="GBK")
            print(f"收到客户端{client_socket}  消息 {recv_str}")
        else:
            for socket_info in client_num:
                # print(socket_info, client_info)
                if socket_info == client_socket:
                    client_num.remove(socket_info)
                    print(f"{socket_info}客户端已经走啦！")
                    break
            print(f" 当前共有客户端 {len(client_num)}")
            break


def accept_client(tcp_serve):
    while 1:
        info = tcp_serve.accept()
        # print(info[0])
        # print(info[1])
        client_num.append(info[0])
        print(f"{info[0]}客户端已经连接！")
        print(f"当前共有客户端{len(client_num)}")

        accept_massage_th = threading.Thread(target=accept_massage, args=(info[0],))
        accept_massage_th.start()
        # accept_massage_th.join()


def send_massage(tcp_serve, massage=""):
    while 1:
        sended_raddr = int(input("给谁发？"))
        for socket in client_num:
            if socket.raddr[1] == sended_raddr:
                massage = input("你要发什么")
                socket.send(massage.edcode())  # 咱是服务器 ，这句话的意思就是 服务器给socket 发 massage
                break
            else:
                print("你还没连上那个客户端了。")
                break


def main():
    tcp_serve = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_serve.bind(SERVE_ADDRESS)
    tcp_serve.listen()
    print("服务器已经启动了！")

    # 创建一个线程 用来接受其他客户端发来的链接请求！
    accept_link = threading.Thread(target=accept_client, args=(tcp_serve,))
    accept_link.start()
    accept_link.join()

    send_th = threading.Thread(target=send_massage, args=(tcp_serve,))
    send_th.start()
    send_th.join()

    if __name__ == '__main__':
        main()
