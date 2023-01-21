import socket

# host and port number
HOST = "subeen.com";
PORT = 80;

# connect the socket
s = socket.socket();
s.connect((HOST,PORT));
# command = 'GET /files/a.txt HTTP/1.1\nHOST: subeen.com\nConnection:close\n\n';

# write a command by document string here
command = \
'''GET /files/a.txt HTTP/1.1
HOST: subeen.com
Connection:close

'''

# send the http request after connecting with host
s.send(command.encode());

while True:
    data = s.recv(512);
    if data == b'':
        break;
    
    print(data.decode());

s.close();

'''
output : 
$ python3 00.socket_request.py 
HTTP/1.1 200 OK
keep-alive: timeout=5, max=100
content-type: text/plain
last-modified: Tue, 14 Sep 2021 13:18:41 GMT
accept-ranges: bytes
content-length: 84
date: Sat, 21 Jan 2023 17:09:59 GMT
server: LiteSpeed
vary: User-Agent,User-Agent
referrer-policy: 
x-turbo-charged-by: LiteSpeed
connection: close

This is a text file.
Congratulations for making a successful connection!
Great job!!
'''