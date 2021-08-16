import socket
import threading

class http_server():
    def __init__(self):
        new_http_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        new_http_server.bind(("192.168.30.1",9090))
        new_http_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
        new_http_server.listen(65535)
        self.new_http_server = new_http_server

    @staticmethod
    def handle_tcp_client(new_client, ip_port):
        while True:
            recv_data = new_client.recv(1024)
            if recv_data:
                recv_content = recv_data.decode('gbk')
                print('接受到来自客户端', ip_port, '的数据:', recv_content)

                response_line = 'HTTP/1.1 200 OK\r\n'
                response_header = 'Server: JSP3/2.0.14\r\n'
                response_body = '这是响应报文\r\n'
                response_content = response_line + response_header + '\r\n' + response_body
                response_data = response_content.encode('gbk')
                new_client.send(response_data)
            else:
                print('客户端', ip_port, '已经断开连接:')
                break
        new_client.close()

    def start(self):
        while True:
            new_client,ip_port = self.new_http_server.accept()
            new_server_thread = threading.Thread(target=self.handle_tcp_client,args=(new_client,ip_port))
            new_server_thread.setDaemon(True)
            new_server_thread.start()


if __name__ == '__main__':

    web = http_server()
    web.start()

