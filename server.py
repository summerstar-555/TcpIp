import socket  # 导入 socket 模块
import os


def run1():
    s = socket.socket()  # 创建 socket 对象
    host = '192.168.213.1'
    print('服务端ip：', host)
    port = 8888  # 设置端口
    s.bind((host, port))  # 绑定端口
    print('等待连接中：')
    s.listen(1)  # 等待客户端连接
    c, addr = s.accept()  # 建立客户端连接
    while True:
        print('用户成功连接！')
        print('连接地址：', addr)
        msg = c.recv(1024).decode('utf-8')
        print(msg)
        if msg == 'quit':
            c.close()
            break
        str1 = input('>>>')
        c.send(str1.encode('utf-8'))
        str1 = input('>>>')
        c.send(str1.encode('utf-8'))


run1()
