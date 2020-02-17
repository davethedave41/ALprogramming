import socket
import sys

try:
    s = socket.socket()
    print("Socket succesfully created")
except socket.error as err:
    print("socket creation failed with error {}".format(err))

# default port for socket
port = 12345
# bind the port to the first computer that requests
# to this network
s.bind(('', port))
print("socket binded to {}".format(port))

# put the socket into listening mode
s.listen(5)
print("socket is listening")

# loops forever until we interrupt it or an
# error occurs
while True:
    # establish a connection with the client
    c, addr = s.accept()
    print('Connection req from -> {}'.format(addr))
    # send msg to client
    str2byte = 'Thank you for connecting cya'
    c.send(str2byte.encode(encoding='utf-8', errors='strict'))
    # close the connection with the client
    c.close()

#try:
#    host_ip = socket.gethostbyname('www.google.com')
#except socket.gaierror:
#    #could not resolve the host
#    print("there was an error resolving the host")
#    sys.exit()

# connecting to the server
# s.connect((host_ip, port))

# print("the socket has succesfully connected to google \
# on port == {}".format(host_ip))
