import socket

#Connection to the server
ip = "vlbelintrocrypto.hevs.ch"
port = 6000

def createMessage(message):


while(True):
    client_socket = socket.socket()
    client_socket.connect((ip,port))


    header = bytes("ISCt", 'utf-8')
    length = bytes([0,1])
    message1 = bytes([0,0,0])
    message2 = bytes("Z", 'utf-8')
    message = header + length + message1 + message2



    client_socket.send(message)  # send message

    data = client_socket.recv(1024) # receive response
    print(data)
