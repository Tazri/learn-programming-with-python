import socket

# host and port number
HOST = "subeen.com";
PORT = 80;

# connect the socket
s = socket.socket();
s.connect((HOST,PORT));
command = 'GET /files/a.txt HTTP/1.1\nHOST: subeen.com\nConnection:close\n\n';
s.send(command.encode());

while True:
    data = s.recv(512);
    if data == b'':
        break;
    
    print(data.decode());

s.close();