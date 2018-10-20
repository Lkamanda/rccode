import socket

def tcp_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    addr = ("127.0.0.1", 8998)
    sock.connect(addr)
    msg = "i am client "
    sock.send(msg.encode())
    rst = sock.recv(500)
    print(rst.decode())
    sock.close()

if __name__ == '__main__':
    tcp_client()