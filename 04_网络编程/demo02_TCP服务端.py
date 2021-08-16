import socket

if __name__ == '__main__':
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 端口号复用，服务器异常退出后,端口号立即释放
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind(("", 9090))
    # listen后的套接字是被动套接字，只负责和客户端连接，不能收发消息
    tcp_server_socket.listen(65535)

    # 当客户端和服务端链接成功时，会返回一个元组，第一个元素是服务器端新建的套接字，第二个元素是客户端的ip和端口
    # 返回的套接字用于服务后面第二个元素中的ip和端口,socket只负责和客户端连接，并且产生一个新的套接字用来和客户端传递数据
    new_client, ip_port = tcp_server_socket.accept()
    print('客户端ip和端口是:', ip_port)

    recv_data = new_client.recv(1024)
    recv_content = recv_data.decode('gbk')
    print('来自客户端的数据是：', recv_content)

    send_content = '问题处理中....'
    send_data = send_content.encode('gbk')
    new_client.send(send_data)

    # 关闭服务于客户端的套接字
    # 当服务端关闭socket，客户端recv会阻塞，传递给recv的数据长度是0，客户端器以此判断服务器已经下线
    new_client.close()

    # 关闭服务器端的套接字，新的客户端无法链入，但是已经连接的套接字仍然可以继续工作
    # 当服务端关闭socket，客户端recv会阻塞，传递给recv的数据长度是0，客户端器以此判断服务器已经下线

    #服务器端一般不关闭
    # tcp_server_socket.close()
