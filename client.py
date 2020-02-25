import socket

# create the socket object
s = socket.socket()

# port that we want to befriend
port = 12345

# connect to the server on local computer
s.connect(('127.0.0.1',port))

# receive data from the server
print(str(s.recv(1024)))
# close the connection
s.close()
