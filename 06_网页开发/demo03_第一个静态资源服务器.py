import socket

if __name__ == '__main__':
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server_socket.bind(("127.0.0.1",9009))
    tcp_server_socket.listen(65535)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)

    while True:
        new_client_socket,ip_port = tcp_server_socket.accept()
        recv_data = new_client_socket.recv(4096)
        recv_content = recv_data.decode('utf-8')
        print('接收到来自用户',ip_port,'的数据：',recv_content)

        #打开文件，写入变量中
        with open("static/index.html") as file:
            file_data = file.read()

        #按照http协议格式书写报文
        respons_line = 'HTTP/1.1 200 OK\r\n'
        respons_header = 'Server: nginx\r\n'
        respons_body = file_data

        response = (respons_line + respons_header + '\r\n' + respons_body)
        response_data = response.encode('utf-8')

        new_client_socket.send(response_data)

    tcp_server_socket.close()