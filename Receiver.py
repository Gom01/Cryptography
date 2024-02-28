import socket

#Connection to the server
IP = "vlbelintrocrypto.hevs.ch"
PORT = 6000

# Decode the message
def decode_message(message):
    type = chr(message[3])
    res = ''

    if type == 't':
        message = message [6:] #remove 6first
        for i in range(len(message)):
            if (i + 1) % 4 == 0:
                res += message[i].to_bytes(1, byteorder='big').decode("utf-8") #Why convert to byte and convert back in Chr
        
    return res
        


client_socket = socket.socket()
client_socket.connect((IP,PORT))

#Listening the server responses
while True:
    data = client_socket.recv() # receive response
    message = decode_message(data)
    print(message)
