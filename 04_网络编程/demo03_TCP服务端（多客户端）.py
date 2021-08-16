import socket
import threading

def handle_tcp_client(new_client,ip_port):
    while True:
        recv_data = new_client.recv(1024)
        if recv_data:
            recv_content = recv_data.decode('gbk')
            print('接受到来自客户端', ip_port, '的数据:', recv_content)

            send_content = '已经收到:正在处理...'
            send_data = send_content.encode('gbk')
            new_client.send(send_data)
        else:
            print('客户端',ip_port,'已经断开连接:')
            break
    new_client.close()

if __name__ == '__main__':
    tcp_server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server_sock.bind(('192.168.30.1',9090))
    tcp_server_sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    tcp_server_sock.listen(128)
    while True:
        new_client,ip_port = tcp_server_sock.accept()
        tcp_thread = threading.Thread(target=handle_tcp_client,args=(new_client,ip_port))
        tcp_thread.start()

    tcp_server_sock.close()
