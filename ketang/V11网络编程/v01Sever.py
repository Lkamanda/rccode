'''
Sever 端流程
            ce1. 建立socket,socket时负责具体通信的一个实例
            2. 绑定，为创建socket指派固定的端口和ip地址
            3.接受对方发送的内容
            4.给对方发送反馈，此步骤为非彼必须步骤
'''
# socket模块负责socket编程

import socket
def serverFunc():
    # ce1.建立socket

    # socket.AF_INET：使用ipv4协议族
    # socket.SOCK_DGRAM：使用UDP通信

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2.绑定ip和ip合port
    # 127.0.0.ce1：这个ip地址是代表的是机器本身
    # 7852: 自定义的端口号
    # 地址是一个tuple类型（ip,port)
    addr = ("127.0.0.ce1", 7852)
    sock.bind(addr)

    # 接收对方的消息
    # 等待方式为死等，没有其他可能
    # recvfrom 接受的返回执是一个tuple,前一项是数据，后一项表示地址
    # 参数的含义是缓冲区的大小
    # rst = sock.recvfrom(500)
    data, addr = sock.recvfrom(500)
    print(data)
    print(type(data))
    # 发送过来的数据是bytes格式,必须通过解码才能得到str格式内容
    # decode 默认参数是utf-8
    # 解码
    text = data.decode()
    print(type(text))
    print(text)
    # 给对方返回的消息
    rsp = "我不饿"
    # 编码
    # 发送的数据需要编码成bytes格式
    # 编码和解码必须一致
    # 默认为utf-8
    data = rsp.encode()
    sock.sendto(data, addr)
if __name__ == '__main__':
    print("starting server")
    serverFunc()
    print("ending server")
