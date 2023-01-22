from socket import *

# creating server by python
server_socket = socket(AF_INET,SOCK_STREAM);
server_socket.bind(("localhost",8888));
server_socket.listen(5);

