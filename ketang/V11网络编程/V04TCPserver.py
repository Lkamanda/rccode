import socket

def tcp_server():
    # TCP协议: socket.SOCK_STREAM
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ("127.0.0.1", 8998)
    sock.bind(addr)
    # 监听接入的访问socket
    sock.listen()

    while True:
        #  接受访问的socket,可以理解接受访问
        # accept接收返回的元组第一个元素赋值给skt,第二个给addr
        skt, addr = sock.accept()
        # 接受对方的发送切得内容利用socket接收内容
        # 500 代表接收使用buffersize
        msg = skt.recv(500)
        msg = msg.decode()
        rst = "Recvied msg:{0}from {1}".format(msg, addr)
        print(rst)
        skt.send(rst.encode())
        skt.close()

if __name__ == '__main__':
    tcp_server()