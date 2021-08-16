import socket

if __name__ == '__main__':
    #客户端也能绑定端口号，bind（），但是没必要

    tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_client_socket.connect(("192.168.30.1",9090))
    send_content = '来自pycharm的测试'
    send_data = send_content.encode("gbk")

    tcp_client_socket.send(send_data)

    #1024是每次可以接受的最大字节
    recv_data = tcp_client_socket.recv(1024)

    #默认收到的数据直接打印前面会有b，表示是二进制，需要转码，国际编码标准是utf-8
    recv_content = recv_data.decode("gbk")
    print('接收到服务器的数据是:',recv_content)

    #当客户端关闭socket，服务器端recv会阻塞，传递给recv的数据长度是0，服务器以此判断客户已经下线，反之，关闭服务器的socket也是一样
    tcp_client_socket.close()


