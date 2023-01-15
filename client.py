import socket  # 导入 socket 模块


def run2():
    s = socket.socket()  # 创建 socket 对象
    host = '192.168.213.1'
    port = 8888  # 设置端口号
    s.connect((host, port))
    while 1:
        str1 = input('>>>')
        s.send(str1.encode('utf-8'))
        msg = s.recv(1024).decode('utf-8')
        print(msg)


run2()
