import socket

# host and port number
HOST = "subeen.com";
PORT = 80;

# create a socket
socket_object = socket.socket()
socket_object.connect((HOST,PORT));

# create a get request command
command = \
'''GET /files/a.txt HTTP/1.1
HOST: subeen.com
Connection:close

'''

socket_object.send(command.encode());

data = socket_object.recv(10);

print(">> first time recv 10 byte data : ");
print(data.decode());

data = socket_object.recv(10);
print("\n>> second time recv 10 byte data : ");
print(data.decode());