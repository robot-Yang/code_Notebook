import socket
import socket
import time
# address = ('192.168.11.159', 10000)
# readdr = ("192.168.11.245", 10000)
address = ('192.168.11.159', 6999)

# 建立一个服务端
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address) #绑定要监听的端口
server.listen(5) #开始监听 表示可以使用五个链接排队
while True:# conn就是客户端链接过来而在服务端为期生成的一个链接实例
    conn,addr = server.accept() #等待链接,多个链接的时候就会出现问题,其实返回了两个值
    print('conn =', conn)
    print('addr =', addr)
    while True:
        try:
            data = conn.recv(1024)  #接收数据
            print('recive:', data.decode()) #打印接收到的数据
            data_sent = 'hhhh'
            # conn.send(data.upper()) #然后再发送数据
            conn.send(data_sent.encode('utf-8'))
            time.sleep(0.5)
        except ConnectionResetError as e:
            print('关闭了正在占线的链接！')
            break
    conn.close()