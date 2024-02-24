import socket

#Connection to the server
IP = "vlbelintrocrypto.hevs.ch"
PORT = 6000

def decode_message(message):
    type = chr(message[3])
    res = ''

    if type == 't':
        message = message [6:]
        for i in range(len(message)):
            if (i + 1) % 4 == 0:
                res += message[i].to_bytes(1, byteorder='big').decode("utf-8")
        
    return res
        


client_socket = socket.socket()
client_socket.connect((IP,PORT))

while True:
    data = client_socket.recv(1024) # receive response
    message = decode_message(data)
    print(message)
