import socket

def serverFunc():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr = ("127.0.0.ce1", 7852)
    sock.bind(addr)
    data, addr = sock.recvfrom(500)
    text = data.decode()
    print(text)
    rsp = "反馈信心"
    data = rsp.encode()
    sock.sendto(data, addr)
if __name__ == '__main__':
    import time
    while True:
        try:
            serverFunc()
        except Exception as e:
            print(e)
        time.sleep(1)
