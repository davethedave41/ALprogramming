import requests, socket, signal,sys, time, re, threading, signal, datetime

# sys.argv gets the arguments from the command line
if len(sys.argv) == 2:
    # input -> python mserver.py <port_no>
    port = int(sys.argv[1])
else:
    # default port
    port = 8080
logger_file_name = 'log.txt'

class Mserver:
    def __init__(self):
        # make it so it stops on Ctrl+C
    #    signal.signal(signal,SIGINT, self.shutdown)
        try:
            # Create a TCP socket
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Re-use the Socket
            self.s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
        except socket.error as s_err:
            message = 'Unable to create/re-use the socket. Error: {}'.format(s_err)
            print(message)
            #

        # bind the socket to a local host and a port
        self.s.bind(('127.0.0.1', port))
        # print('socket binded to {}'.format(port))
        # server socket allowing up to 10 client connections
        self.s.listen(7)
        message = str(datetime.datetime.now())+'\n'

        message = '\nHost Name: Localhost\nHost address: 127.0.0.1\nHost port: '+str(port)+'\n'
        print(message)

        print('Server is ready to listen to clients\n')

# class threading.Thread(group=None, target=None, name=None, args=(),
#                kwargs={}, *, daemon=None)  threading class parameters

# socket.getaddrinfo(host, port[, family[, socktype[, proto[, flags]]]])
# Translate the host/port argument into a sequence of 5-tuples that contain all the necessary # arguments for creating a socket connected to that service. host is a domain name, a string #  representation of an IPv4/v6 address or None. port is a string service name such as
# 'http', a numeric port number or None. By passing None as the value of host and port, you can pass NULL # to the underlying C API.
    def listen_to_client(self):
        ''' waiting for clients to connect over tcp to the
        proxy server'''
        while True:

            # Establish the connection -> accept connetions from outside
            (clientSocket, client_address) = self.s.accept()
            # printing the relevant client details on the server side
            client_details_log = '-----------the book of facts-----------\n'
            client_details_log += 'Client host name: '+str(client_address[0])+'\
            \nClient port number: '+str(client_address[1])+'\n'
            client_socket_details = socket.getaddrinfo(str(client_address[0]),
            client_address[1])
            # print(client_sockocket_details)
            client_details_log += 'Socket family: '+str(client_socket_details[0][0])+'\n'
            client_details_log += 'Socket type: '+str(client_socket_details[0][1])+'\n'
            client_details_log += 'Timeout: '+str(clientSocket.gettimeout())+'\n'
            client_details_log += '-----------------------------------------\n'
            self.log_info(client_details_log)
            # Logging
            message = 'Client IP address: '+str(client_address[0])+' and Client port \
                       number: '+str(client_address[1])+'\n'

            # creating a new thread for every client
            d = threading.Thread(name = str(client_address),
            target = self.proxy_thread, args=(clientSocket, client_address))
            d.setDaemon(True)
            d.start()

        self.s.close()
    def multi_threading(self,client_sock,client_address):
        print(str(datetime.datetime.now()))
        # 'v' is an arrow down
        print('New connection \'v\'\nClient address: '+str(client_address[0])+'\
        \nClient port number: '+str(client_address[1]))
        # starting timer to calculate elapsed time
        start_time = time.time()
        # getting client request
        client_request = client_sock.recv(1024)
        # if the client request is not empty
        if client_request:
            # getting request length
            request_length = len(client_request)
            message = 'Request Size: '+str(request_length)+' bytes\n'

            print(message)
            # parsing the request line and headers sent by the client
            # since the request will be of the form GET http://www.dave.com HTTP/1.1 extracting the http part
            print('CLIENT REQ: '+str(client_request))
            try:
                response = str(client_request).split(' ')[0].split('\'')[1]
                print('\nREQ TYPE: '+str(response))
            except IndexError:
                response = str(client_request).split(' ')[0].split('\"')[1]
                print('\nREQ TYPE: '+str(response))
            if response == 'GET':
                http_part = str(client_request).split(' ')[1]
                print('HTTP/HTTPS: '+http_part)
                #stripping the http part to get only the URL and removing the trailing / from the request
                double_slash_pos = str(http_part).find('//')
                url_connect = ''
                url_slash_check = list()
                url_slash = str()
                # if no http part to the url
                if double_slash_pos == -1:
                    url_part = http_part[1:]
                    print('URL: '+url_part)
                    # getting the www.dave.com part
                    url_connect = url_part.split('/')[0]
                else:
                    # if the url ends with / removing it e.g www.dave.com/
                    if http_part.split('//')[1][-1] == '/':
                        url_part = http_part.split('//')[1][:-1]
                        # removing the '/'
                        print('URL: '+url_part+'\n')
                        url_connect = url_part.split('/')[0]
                        #print('URL: '+url_connect+'\n')
                    else:
                        url_part = http_part.split('//')[1]
                        print('URLd: '+url_part)
                        #getting the www.dave.com part
                        url_connect = url_part.split('/')[0]
                # url_connect = url_part
                # getting the part after the host --> TLD
                url_slash_check = url_part.split('/')[1:]
                url_slash = ''
                if url_slash_check:
                    for path in url_slash_check:
                        # every domain after TLD
                        url_slash += '/'
                        url_slash += path
                # checking if port number is provided
                client_req_port_start = str(url_part).find(':')
                # if not use default port no
                port_number = 80
                # replacing all non alpha numeric characters with underscore using regexp lib
                url_file_name = re.sub('[^0-9a-zA-Z]+','_', url_part)
                # no port specified
                if client_req_port_start == -1:
                    pass
                else:
                    # port given in client request
                    port_number = int(url_part.split(':')[1])
                self.proxy_http(url_file_name, client_sock, port_number,
                client_address, start_time, url_connect, url_slash)
            else:
                # not a GET command
                message = 'Client with port: ' +str(client_address[1])+ '''generated
                a call other than GET: '''+ response +'\n'
                print(message)
                client_sock.send(b'HTTP/1.1 405 Method Not Allowed\r\n\r\n')
                client_sock.close()
                message = 'HTTP/1.1 405 Method Not Allowed\r\n\r\n'

        else:
            # blank request call by client
            client_sock.send('')
            print('Empty message\n')
            client_sock.close()
            message = 'Client with port: '+str(client_address[1])+'\nConnection CLOSED\n'
            print(message)
        #

    def proxy_http(self, url_file_name, client_sock, port_number, client_address,
                  start_time, url_connect, url_slash):
        try:
            # getting the cached file for the url if it exists
            cached_file = open(url_file_name, 'r')
            # reading the contents of the file
            message = 'Client with port: '+str(client_address[1])+'\nCACHE HIT'
            print(message)

            # get proxy server details from cache
            server_socket_details = socket.getaddrinfo('Localhost', port_number)
            server_details_message = '<body> Cached Server Details:- <br />'
            server_details_message += '''Server host name: localhost <br /> Server port number: '''+str(port_number)+'<br>'
            server_details_message += 'Socket family: '+str(server_socket_details[0][0])+ '<br>'
            server_details_message += 'Socket type: '+str(server_socket_details[0][1])+ '<br>'
            server_details_message += 'Socket protocol: '+str(server_socket_details[0][2]) + '<br>'
            server_details_message += 'Timeout: '+str(client_sock.gettimeout())+'<br> </body>'
            response_message = ''
            # print 'reading data line by line and appending it'
            with open(url_file_name) as f:
                for line in f:
                    response_message += line
            # appending the server details message to the response
            # response_message += server_details_message
            #closing the file handler
            cached_file.close()
            # sending the cached data
            client_sock.send(response_message.encode('utf8'))
            end_time = time.time()
            message = 'Response Length: '+str(len(response_message))+ 'bytes'
            print(message)
            message = 'Time Elapsed(RTT): '+str(end_time - start_time)+' seconds'
            print(message)


        except IOError as e:
            message = 'Client with port: '+str(client_address[1])+'\nCACHE MISS'
            print(message)
            '''there is no cached file for the specified URL from the proxy server and
            cache it. To get the URL we nedd to create a socket on proxy machine'''
            proxy_sock = None
            try:
                # creating socket from proxy server
                proxy_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            except socket_error as s_err:
                print('Unable to create the socket. Error: {}'.format(s_err))
                message = 'Unable to create the socket. Error: {}'.format(s_err)
            try:
                # setting time out so that after the last packet if no other packet comes socket will auto close in 2 seconds
                proxy_sock.settimeout(2)
                # connecting to the url specified by the client
                proxy_sock.connect((url_connect, port_number))
                # sending GET request from client to the web server
                web_request = str()
                if url_slash: # url_slash is other than None
                    web_request = 'GET /'+url_slash[1:]+' HTTP/1.1\r\nHost: '+url_connect+'\r\n\r\n'
                else:
                    web_request = 'GET / HTTP/1.1 \r\nHost: '+str(url_connect)+'\r\n\r\n'
                    print('Just TLD domain, no other slashes')
                # send web request to server
                proxy_sock.send(web_request.encode('utf8'))
                message = 'Request size: '+str(len(web_request))+' bytes'
                print(message)
                message = 'REQ to server as: GET / HTTP/1.1 \nHost: '+str(url_connect)
                print(message)
                # getting the web server response which is expected to be a file
                server_socket_details = socket.getaddrinfo(url_connect, port_number)
                server_details_message = '<body> Web Server Details:- <br />'
                server_details_message += 'Server host name: '+url_connect+''' <br /> \nServer port number:  '''+str(port_number)+'<br />\n'
                server_details_message += 'Socket family: ' + str(server_socket_details[0][0]) + '<br />'
                server_details_message += 'Socket type: ' + str(server_socket_details[0][1]) + '<br />'
                server_details_message += 'Socket protocol: ' + str(server_socket_details[0][2]) + '<br />'
                server_details_message += 'Timeout: '+str(client_sock.gettimeout())+'<br /> </body>\n'
                # use this variable to get the web's response message and check if it is empty in the loop incase there is no response from the server
                append_response = ''
                # timeout flag incase there is a timeout after 2 seconds of waiting
                timeout_flag = False
                while True:
                    try:
                        web_serv_resp = proxy_sock.recv(4096)
                    except socket.timeout:
                        # a time out occurred on waiting for server response so break
                        # out of loop
                        if len(append_response) <= 0:
                            timeout_flag = True
                        break
                    if len(web_serv_resp) > 0:
                        append_response += str(web_serv_resp)
                    else:
                        # all the data has been received
                        break
                # print('Data: '+append_response)
                # variable to store response to file
                response_to_file = append_response
                # storing the response from the webserver to the client locally
                append_response += str(server_details_message)
                if timeout_flag:
                    # timeout ocurred
                    err_resp = 'HTTP/1.1 408 Request timeout \r\n\r\n'
                    print('HTTP/1.1 408 Request timeout')
                    # err_resp += serv_deets
                    client_sock.send(err_resp.encode('utf8'))
                else:
                    # sending the web server response back to the client
                    client_sock.send(web_serv_resp)
                end_time = time.time()
                message = 'Time Elapsed(RTT): '+str(end_time- start_time)+' seconds'
                print(message)
                # caching the response on the proxy server
                proxy_temp_file = open(url_file_name, 'wb')
                # writing entire response to file
                proxy_temp_file.write(response_to_file.encode('utf8'))
                proxy_temp_file.close()
                message = 'Response size: '+str(len(response_to_file))+' bytes\n'
                # closing the proxy server socket
                proxy_sock.close()
            except:
                # sending page not found response to client
                error_msg = ''
                '''if str(e) == 'timed out:'
                error_msg = 'HTTP/1.1 404 Not Found \r\n'
                client_sock.send('HTTP/1.1 408 Request timeout \r\n\r\n')
                else:'''
                error_msg = 'HTTP/1.1 404 Not Found \r\n\r\n'
                print('HTTP/1.1 404 Not Found\n')
                client_sock.send(b'HTTP/1.1 404 Not Found \r\n\r\n')
                end_time = time.time()
                message = 'ERROR : '+str(e)+'\n'
                print(message)
                message = 'Response sent: '+error_msg+' \n'
                print(message)
                message = 'Time Elapsed(RTT): '+str(end_time - start_time)+' seconds \n'
                print(message)
        # closing the connection with client
        client_sock.close()
        message = 'Connection CLOSED \n'
        print(message)

    def proxy_https():


if __name__ == '__main__': # if running this through the command line then run this
    # creating the instance of the server class
    server = Mserver()
    server.listen_to_client()
