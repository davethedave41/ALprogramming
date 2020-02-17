import requests, socket, signal,sys, time, re

# sys.argv gets the arguments from the command line
if len(sys.argv) == 2:
    # input -> python mserver.py <port_no>
    port = int(sys.argv[1])
else:
    # default port
    port = 8080
logger_file_name = "log.txt"

class Mserver:
    def __init__(self):
        # make it so it stops on Ctrl+C
        #signal.signal(signal,SIGINT, self.shutdown)
        try:
            # Create a TCP socket
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Re-use the Socket
            self.s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
        except error as e:
            message = 'Unable to create/re-use the socket. Error: {}'.format(e)
            print(message)
            #self.log_info(message)

        # bind the socket to a local host and a port
        self.s.bind(('', port))
        print("socket binded to {}".format(port))
        # server socket allowing up to 10 client connections
        self.s.listen(7)
        message = "Host Name: Localhost and Host address: 127.0.0.1 and Host port:\
        "+str(port) + "\n"
        #self.log_info(message)
        print('Server is ready to listen to clients')

# class threading.Thread(group=None, target=None, name=None, args=(),
#                kwargs={}, *, daemon=None)  threading class parameters

# socket.getaddrinfo(host, port[, family[, socktype[, proto[, flags]]]])
# Translate the host/port argument into a sequence of 5-tuples that contain all the necessary # arguments for creating a socket connected to that service. host is a domain name, a string #  representation of an IPv4/v6 address or None. port is a string service name such as
# 'http', a numeric port number or None. By passing None as the value of host and port, you can pass NULL # to the underlying C API.
    def listen_to_client(self):
        """ waiting for dumbass client to connect over tcp to there
        proxy server"""
        while True:

            # Establish the connection -> accept connetions from outside
            (clientSocket, client_address) = self.s.accept()
            print(client_address)
            # printing the relevant client details on the server side
            client_details_log = "-----------the book of facts-----------\n"
            client_details_log += "Client host name: "+str(client_address[0])+"\
            \nClient port number: "+str(client_address[1])+"\n"
            client_socket_details = socket.getaddrinfo(str(client_address[0]),
            client_address[1])
            # print(client_socket_details)
            client_details_log += "Socket family: "+str(client_socket_details[0][0])+"\n"
            client_details_log += "Socket type: "+str(client_socket_details[0][1])+"\n"
            client_details_log += "Timeout: "+str(clientSocket.gettimeout())+"\n"
            client_details_log += "-----------------------------------------\n"
            #self.log_info(client_details_log)
            # Logging
            message = "Client IP address: "+str(client_address[0])+" and Client port \
                       number: "+str(client_address[1])+"\n"
            # self.log_info(message)
            # creating a new thread for every client
            d = threading.Thread(name = str(client_address),
            target = self.proxy_thread, args=(clientSocket, client_address))
            d.setDaemon(True)
            d.start()

        self.s.close()
    def proxy_thread(self,client_s,client_address):
        print('New thread given to new connection')
        # starting timer to calculate elapsed time
        start_time = time.time()
        # getting client request
        client_request = client_s.recv(1024)
        # if the client request is not empty
        if client_request:
            # getting request length
            request_length = len(client_request)
            message = "Client with port: "+str(client_address[1])+"request length is\
            "+str(request_length)+"\bytes \n"

            # parsing the request line and headers sent by the client
            # since the request will be of the form GET http://www.pornhub.com HTTP/1.1 extracting the http part
            resp_part = client_request.split(' ')[0]
            if resp_part == 'GET':
                http_part = client_request.split(' ')[1]
                #stripping the http part to get only the URL and removing the trailing / from the request
                double_slash_pos = str(http_part).find('//')
                url_connect = ''
                url_slash_check = list()
                url_slash = str()
                # if no http part to the url
                if double_slash_pos == -1:
                    url_part = http_part[1:]
                    # getting the www.pornhub.com part
                    url_connect = url_part.split('/')[0]
                else:
                    # if the url ends with / removing it e.g www.pornhub.com/
                    if http_part.split('//')[1][-1] == "/":
                        url_part = http_part.split('//')[1][:-1]
                        # removing the '/'
                        url_connect = url_part.split('/')[0]
                    else:
                        url_part = http_part.split('//')[1]
                        # getting the www.pornhub.com part
                        url_connect = url_part.split('/')[0]
                # getting the part after the host --> TLD
                url_slash_check = url_part.split('/')[1:]
                url_slash = ''
                if url_slash_check:
                    for path in url_slash_check:
                        # every domain after TLD
                        url_slash += '/'
                        url_slash += path
                # checking if port number is provided
                client_req_port_start = str(url_part).find(":")
                # if not use default port no
                port_number = 80
                # replacing all non alpha numeric characters wiht underscore
                url_file_name = re.sub('[^0-9a-zA-Z]+','_', url_part)
                if client_req_port_start == -1:
                    pass
                else:
                    port_number = int(url_part.split(':')[1])
                self.find_file(url_file_name, client_s, port_number,
                client_address, start_time, url_connect, url_slash)
            else:
                # not a GET command
                message = "Client with port: " +str(client_address[1]+ "generated\
                a call other than GET: "+ resp_part + "\n")
                client_s.send('HTTP/1.1 405 Method Not Allowed\r\n\r\n')
                client_s.close()
                self.log_info(message)
                message = 'HTTP/1.1 405 Method Not Allowed\r\n\r\n'
                self.log_info(message)
        else:
            # blank request call by client
            client_s.send('')
            client_s.close()
            message = 'Client with port: '+str(client_address[1])+'connection closed \n'
            self.log_info(message)

    def find_file(self, url_file_name, client_s, port_number, client_address,
    start_time, url_connect, url_slash):
        try:
            # getting the cached file for the url if it exists
            cached_file = open(url_file_name, 'r')
            # reading the contents of the file
            message = 'Client with port:'+str(client_address[1])+': Cache hit occurred \
            for the request. Reading from file \n'
            self.log_info(message)
            # get proxy server details....
            response_message = ''
            # print 'reading data line by line and appending it'
            with open(url_file_name) as f:
                for line in f:
                    response_message += line
            # print 'finished reading the data'
            # appending the server details message to the response
            # response_message += server_details_message
            #closing the file handler
            cached_file.close()
            # sending the cached data
            
    def log_info(self, message):
        logger_file = open(logger_file_name, 'a')
        logger_file.write(message)
        logger_file.close()
try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:
    # could not resolve the host
    print("there was an error resolving the host")
    sys.exit()
print(sys.argv)
port = 12345
serv = Mserver()
serv.listen_to_client()
print(serv.s)
