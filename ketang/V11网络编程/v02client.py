'''
- Client 端流程
            ce1.建立通信的socket
            2.发送内容到指定服务器
            3.接受服务器给定的反馈内容
'''
import socket

def clientFunc():
    # 建立socket
    # 指定使用ipv4协议 : socket.AF_INET
    # 指定使用UDP通信协议: socket.SOCK_DGRAM
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    Text = 'i am  client '
    # 发送的数据必须是bytes格式
    data = Text.encode()
    # 发送
    sock.sendto(data, ("127.0.0.ce1", 7852))

    data, addr = sock.recvfrom(200)

    data = data.decode()
    print(data)
if __name__ == '__main__':
    clientFunc()
