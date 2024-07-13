import socket

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('localhost',9999))

server.listen(1)
client,address=server.accept()

done=False

while not done:

    msg=client.recv(1024).decode('utf-8')

    if msg=='quit':
        done=True
        break
    else:
        print(msg)
        client.send(input('MESSAGE:').encode('utf-8'))

server.close()
client.close()
    