Chapter 14 : Socket Programming
===============================

## About Socket 

- When a software load in the ram then it start to work it called **process.**
- Use **socket** for communicate process each others.
- When communicate other computer process then must be know **port** where it run with computer ip. 
- A Port number is between **1 to 65535.**
- Web server run on port 80.
- Use port 80 for **HTTP**.
- Use port 443 for **HTTPS**


<hr />
<br />

## Socket Package
create a socket syntax : 
```py
import socket

s = socket.socket(); # create a socket for IPv4 by default

```

Need to 3 thing to create a socket in python is : 
- IP address
- PORT number
- Protocol

connecting with secket by host and port : 
```py
import socket

s = socket.socket();
s.connect((Host,PORT));
```

sending a method by following http protocol after connect the scokect. Here s is socket object : 
```py
command = 'GET /files/a.txt HTTP/1.1\nHOST: subeen.com\nConnection:close\n\n';

# must be send a message as a binary. so encode it
s.send(command.encode());
```

It possible to write the command like this : 
```py
command = \
'''GET /files/a.txt HTTP/1.1
HOST: subeen.com
Connection:close

'''

command = command.encode(); # encode it in binary
```

Receiving data from socket object after sending command by **.send** method. Here **s** is **socket.socket()**.
```py
data = s.recv(buffer_size) # get data in binary format

# get the whole data
while data != b'' : 
    data = s.recv(buffer_size); # get data in binary format

```

Close the connect after creating connection with server. Here **s** is **socket.socket()**.
```py
s.close();
```

## Example of socket object by HTTP get request
```py
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
```

<hr />
<br />

[< Go Back](./../part_4.md)
--------------------------